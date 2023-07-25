# ONS-Coronasurveys

Identifying differences between [ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveyheadlineresultsuk) and [Coronasurveys](https://coronasurveys.org) COVID-19 case count estimates

## Methodology

Data was gathered from the links above and stored to [data/raw/](./data/raw/).
Coronasurveys regional data for England (ENG), Northern Ireland (NIR), Wales (WLS), and Scotland (SCT) track the total percentage of cases, while the ONS data tracks only the percentage of active infected cases.
We also included the dataset for all regions from the Coronasurveys project, which tracks active infected cases.
This data was then processed by either [coronasurveys.R](./src/coronasurveys.R) or [ons.R](./src/ons.R) to remove unnecessary columns and format percentages as a number out of 100.
The processed data can be found in [data/processed/](./data/processed/).
The [filter.R](./src/filter.R) script (or the [filter-gb.R](./src/filter-gb.R) script in the case of the Coronasurveys data for the entire UK) was used to eliminate `NA` values from the data and leave only days where both the Coronasurveys and ONS datasets were complete.
This data, used for generating plots, is available at [data/filtered/](./data/filtered/).

## Plots

To see all plots generated from the filtered datasets, run [plot.py](./src/plot.py).
If you're using Poetry, running `poetry install` will install all the required dependencies.
Otherwise, you can run `pip install -r requirements.txt` to install the dependencies.
A sample of some of the most interesting views can be found in [plots/](./plots/).
