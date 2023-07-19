# Processes ons-combined.csv and divides it into 4 files for each region:
# 1. ons-eng.csv
# 2. ons-wls.csv
# 3. ons-nir.csv
# 4. ons-sct.csv

# imports
library(data.table)

# read in ons-combined.csv
'Reading ons-combined.csv …'
ons <- fread('data/raw/ons-combined.csv')

# partition by region
'Partitioning ons-combined.csv by region …'
ons_eng <- ons[region == 'eng']
ons_wls <- ons[region == 'wls']
ons_nir <- ons[region == 'nir']
ons_sct <- ons[region == 'sct']

# remove region columns
'Extracting data …'
ons_eng[, region := NULL]
ons_wls[, region := NULL]
ons_nir[, region := NULL]
ons_sct[, region := NULL]

# remove duplicates
'Filtering out duplicate dates …'
ons_eng <- ons_eng[!duplicated(ons_eng$date)]
ons_wls <- ons_wls[!duplicated(ons_wls$date)]
ons_nir <- ons_nir[!duplicated(ons_nir$date)]
ons_sct <- ons_sct[!duplicated(ons_sct$date)]

# write out files
'Writing output to data/processed/ons-{region}.csv …'
write.csv(ons_eng, 'data/processed/ons-eng.csv', quote = FALSE, row.names = FALSE)
write.csv(ons_wls, 'data/processed/ons-wls.csv', quote = FALSE, row.names = FALSE)
write.csv(ons_nir, 'data/processed/ons-nir.csv', quote = FALSE, row.names = FALSE)
write.csv(ons_sct, 'data/processed/ons-sct.csv', quote = FALSE, row.names = FALSE)

'Done!'
