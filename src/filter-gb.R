# Collects data across similar dates nationally:
# coronasurveys (gb)
# ons (computed national average of eng, wls, nir, sct)

# imports
library(data.table)

fetch <- function(region) {    
  # read in ONS regional data
  if (region == 'gb') {
    coronasurveys <- fread('data/processed/coronasurveys-gb.csv')
    return(coronasurveys)
  }
  ons <- fread(sprintf('data/processed/ons-%s.csv', region))
  ons
}

days <- function(x) {
  # replace date strings with days since 2020/01/06
  x$date <- as.Date(x$date)
  x$days <- as.numeric(x$date - as.Date('2020/01/06'))
  x[, date := NULL]
}

sort <- function(x) {
  # sort by date
  x[order(x$days)]
}

filter <- function(coronasurveys, ons) {
  # filter coronasurveys and ons datasets by removing days with no data in either set
  coronasurveys.max <- max(coronasurveys$days)
  ons.max <- max(ons$days)
  min_max <- min(c(ons.max, coronasurveys.max))
  coronasurveys <- coronasurveys[days <= min_max]
  ons <- ons[days <= min_max]

  for (i in 0:min_max) {
    # check slices for existence
    coronasurveys.slice <- coronasurveys[days == i]
    ons.slice <- ons[days == i]
    if (nrow(ons.slice) == 0) coronasurveys <- coronasurveys[!(days == i)]
    if (nrow(coronasurveys.slice) == 0) ons <- ons[!(days == i)]

    # check slices for NA values
    coronasurveys.slice <- coronasurveys.slice[1]
    ons.slice <- ons.slice[1]
    if (
      is.na(ons.slice$p_infected)
      | is.na(ons.slice$p_infected_low)
      | is.na(ons.slice$p_infected_high)
      | is.na(coronasurveys.slice$p_active)
      | is.na(coronasurveys.slice$p_active_low)
      | is.na(coronasurveys.slice$p_active_high)
    ) {
      ons <- ons[!(days == i)]
      coronasurveys <- coronasurveys[!(days == i)]
    }
  }

  list(coronasurveys, ons)
}

write <- function(coronasurveys, ons) {
  # write out files
  write.csv(
    coronasurveys, 'data/filtered/coronasurveys-gb.csv',
    quote = FALSE, row.names = FALSE
  )
  write.csv(
    ons, 'data/filtered/ons-gb.csv',
    quote = FALSE, row.names = FALSE
  )
}

process <- function(region) {
  # main routine for each region
  print(sprintf('Processing %s …', region))
  
  print('  Fetching data …')
  data <- fetch(region)

  print('  Sorting data …')
  data <- days(data)
  data <- sort(data)

  print('  Filtering data …')
  if (region == 'gb') data <- data[, .(p_active, p_active_low, p_active_high, days)]
  else data <- data[, .(p_infected, p_infected_low, p_infected_high, days)]
  data
}

average <- function(regions) {
  # average ONS data across all regional datasets
  if (length(regions) != 4) stop('Invalid number of regions')
  eng.max <- max(regions[[1]]$days)
  wls.max <- max(regions[[2]]$days)
  nir.max <- max(regions[[3]]$days)
  sct.max <- max(regions[[4]]$days)
  max_max <- max(c(eng.max, wls.max, nir.max, sct.max))

  ons <- data.table()
  for (i in 0:max_max) {
    # average data
    slice <- data.table()
    eng.slice <- regions[[1]][days == i]
    wls.slice <- regions[[2]][days == i]
    nir.slice <- regions[[3]][days == i]
    sct.slice <- regions[[4]][days == i]

    if (nrow(eng.slice) != 0) slice <- rbind(slice, eng.slice)
    if (nrow(wls.slice) != 0) slice <- rbind(slice, wls.slice)
    if (nrow(nir.slice) != 0) slice <- rbind(slice, nir.slice)
    if (nrow(sct.slice) != 0) slice <- rbind(slice, sct.slice)

    # average cols in slice
    if (is.null(slice$p_infected)) next
    if (is.null(slice$p_infected_low)) next
    if (is.null(slice$p_infected_high)) next

    p_infected <- mean(slice$p_infected, na.rm = TRUE)
    p_infected_low <- mean(slice$p_infected_low, na.rm = TRUE)
    p_infected_high <- mean(slice$p_infected_high, na.rm = TRUE)

    # add to dataset
    if (
      !is.na(p_infected)
      | !is.na(p_infected_low)
      | !is.na(p_infected_high)
    ) {
      row <- list(
        p_infected = p_infected,
        p_infected_low = p_infected_low, p_infected_high = p_infected_high,
        days = i
      )
      ons <- rbind(ons, row)
    }
  }

  ons
}

REGIONS <- c('eng', 'wls', 'nir', 'sct')
ONS <- list()
sprintf('Preparing ONS regional data for %s …', paste(REGIONS, collapse = ', '))
for (region in REGIONS) ONS <- c(ONS, list(process(region)))
ONS <- average(ONS)
coronasurveys <- process('gb')
'Filtering collected data …'
data <- filter(coronasurveys, ONS)
coronasurveys <- data[[1]]
ONS <- data[[2]]
'Writing filtered results …'
write(coronasurveys, ONS)
'Done!'
