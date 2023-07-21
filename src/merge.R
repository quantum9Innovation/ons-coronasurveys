# Collects data across similar dates in processed files:
# coronasurveys (eng, wls, nir, sct)
# ons (eng, wls, nir, sct)

# imports
library(data.table)

fetch <- function(region) {    
  # read in regional data
  coronasurveys <- fread(sprintf('data/processed/coronasurveys-%s.csv', region))
  ons <- fread(sprintf('data/processed/ons-%s.csv', region))
  list(coronasurveys, ons)
}

days <- function(x) {
  # replace date strings with days since 2020/01/06
  x$date <- as.Date(x$date)
  x$days <- as.numeric(x$date - as.Date('2020/01/06'))
  x[, date := NULL]
}

weeks <- function(x, columns) {
  # merge entries into weeks using day numbers and averaging data
  x[, week := floor(x$days / 7)]
  max <- max(x$week)

  for (i in 0:max) {
    slice <- x[week == i]
    if (nrow(slice) == 0) next

    x <- x[!(week == i)]
    data <- data.table()
    data[, week := i]
    data[, days := 7 * i]

    for (j in 1:length(columns)) {
      col <- columns[j]
      set(data, j = col, value = mean(slice[, get(col)], na.rm = TRUE))
    }

    x <- rbind(x, data)
  }

  x
}

sort <- function(x) {
  # sort by date
  x[order(x$days)]
}

filter <- function(coronasurveys, ons) {
  # filter coronasurveys and ons datasets by removing weeks with no data in either set
  coronasurveys.max <- max(coronasurveys$week)
  ons.max <- max(ons$week)
  min_max <- min(c(ons.max, coronasurveys.max))
  coronasurveys <- coronasurveys[week <= min_max]
  ons <- ons[week <= min_max]

  for (i in 0:min_max) {
    # check slices for existence
    coronasurveys.slice <- coronasurveys[week == i]
    ons.slice <- ons[week == i]
    if (nrow(ons.slice) == 0) coronasurveys <- coronasurveys[!(week == i)]
    if (nrow(coronasurveys.slice) == 0) ons <- ons[!(week == i)]

    # check slices for NA values
    coronasurveys.slice <- coronasurveys.slice[1]
    ons.slice <- ons.slice[1]
    if (
      is.na(ons.slice$p_infected)
      | is.na(ons.slice$p_infected_low)
      | is.na(ons.slice$p_infected_high)
      | is.na(coronasurveys.slice$p_cases)
      | is.na(coronasurveys.slice$p_cases_low)
      | is.na(coronasurveys.slice$p_cases_high)
    ) {
      ons <- ons[!(week == i)]
      coronasurveys <- coronasurveys[!(week == i)]
    }
  }

  list(coronasurveys, ons)
}

write <- function(coronasurveys, ons, region) {
  # write out files
  write.csv(
    coronasurveys, sprintf('data/filtered/coronasurveys-%s.csv', region),
    quote = FALSE, row.names = FALSE
  )
  write.csv(ons, sprintf('data/filtered/ons-%s.csv', region), quote = FALSE, row.names = FALSE)
}

process <- function(region) {
  # main routine for each region
  print(sprintf('Processing %s …', region))
  
  print('  Fetching data …')
  data <- fetch(region)
  coronasurveys <- data[[1]]
  ons <- data[[2]]

  print('  Sorting data …')
  coronasurveys <- days(coronasurveys)
  ons <- days(ons)
  coronasurveys <- sort(coronasurveys)
  ons <- sort(ons)

  print('  Filtering data …')
  coronasurveys <- weeks(coronasurveys, c('p_cases', 'p_cases_low', 'p_cases_high'))
  ons <- weeks(ons, c('p_infected', 'p_infected_low', 'p_infected_high'))
  data <- filter(coronasurveys, ons)
  coronasurveys <- data[[1]]
  ons <- data[[2]]
  print('  Writing data …')
  write(coronasurveys, ons, region)
}

REGIONS <- c('eng', 'wls', 'nir', 'sct')
sprintf('Beginning regions processes for %s …', paste(REGIONS, collapse = ', '))
for (region in REGIONS) process(region)
'Done!'
