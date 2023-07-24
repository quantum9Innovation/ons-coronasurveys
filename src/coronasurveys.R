# Processes coronasurveys regional files and one nationwide file:
# 1. coronasurveys-eng.csv
# 2. coronasurveys-wls.csv
# 3. coronasurveys-nir.csv
# 4. coronasurveys-sct.csv
# 5. coronasurveys-gb.csv (NATIONAL)

# imports
library(data.table)

# read in regional data
'Reading regional datasets …'
eng <- fread('data/raw/coronasurveys-eng.csv')
wls <- fread('data/raw/coronasurveys-wls.csv')
nir <- fread('data/raw/coronasurveys-nir.csv')
sct <- fread('data/raw/coronasurveys-sct.csv')

# read in national data
'Loading national datasets …'
gb <- fread('data/raw/coronasurveys-gb.csv')

# pick out data columns
'Extracting data …'
p_eng <- eng[, c('date', 'p_cases', 'p_cases_error')]
p_wls <- wls[, c('date', 'p_cases', 'p_cases_error')]
p_nir <- nir[, c('date', 'p_cases', 'p_cases_error')]
p_sct <- sct[, c('date', 'p_cases', 'p_cases_error')]
gb[, 2:7 := NULL]

# multiply percentages by 100
'Calculating percentages …'
p_eng[, p_cases := p_cases * 100]
p_wls[, p_cases := p_cases * 100]
p_nir[, p_cases := p_cases * 100]
p_sct[, p_cases := p_cases * 100]
p_eng[, p_cases_error := p_cases_error * 100]
p_wls[, p_cases_error := p_cases_error * 100]
p_nir[, p_cases_error := p_cases_error * 100]
p_sct[, p_cases_error := p_cases_error * 100]

# multiply cols 8 to end of gb by 100
for (i in 2:ncol(gb)) gb[, i] <- 100 * gb[, ..i]

# add p_cases_low and p_cases_high columns
'Adding bounds based on error measurements …'
p_eng[, p_cases_low := pmax(p_cases - p_cases_error, 0)]
p_wls[, p_cases_low := pmax(p_cases - p_cases_error, 0)]
p_nir[, p_cases_low := pmax(p_cases - p_cases_error, 0)]
p_sct[, p_cases_low := pmax(p_cases - p_cases_error, 0)]
p_eng[, p_cases_high := pmin(p_cases + p_cases_error, 100)]
p_wls[, p_cases_high := pmin(p_cases + p_cases_error, 100)]
p_nir[, p_cases_high := pmin(p_cases + p_cases_error, 100)]
p_sct[, p_cases_high := pmin(p_cases + p_cases_error, 100)]
p_eng[, p_cases_error := NULL]
p_wls[, p_cases_error := NULL]
p_nir[, p_cases_error := NULL]
p_sct[, p_cases_error := NULL]

# remove duplicates
'Filtering out duplicate dates …'
p_eng <- p_eng[!duplicated(p_eng$date)]
p_wls <- p_wls[!duplicated(p_wls$date)]
p_nir <- p_nir[!duplicated(p_nir$date)]
p_sct <- p_sct[!duplicated(p_sct$date)]
gb <- gb[!duplicated(gb$date)]

# write out files
'Writing output to data/processed/coronasurveys-{region}.csv …'
write.csv(p_eng, 'data/processed/coronasurveys-eng.csv', quote = FALSE, row.names = FALSE)
write.csv(p_wls, 'data/processed/coronasurveys-wls.csv', quote = FALSE, row.names = FALSE)
write.csv(p_nir, 'data/processed/coronasurveys-nir.csv', quote = FALSE, row.names = FALSE)
write.csv(p_sct, 'data/processed/coronasurveys-sct.csv', quote = FALSE, row.names = FALSE)
write.csv(gb, 'data/processed/coronasurveys-gb.csv', quote = FALSE, row.names = FALSE)

'Done!'
