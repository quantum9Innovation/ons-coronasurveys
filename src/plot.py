'''
Generates comparison plots from filtered data.
Data must already exist in data/filtered/ before running.
'''

import pandas as pd
import scienceplots
import matplotlib.pyplot as plt

# setup plots
plt.style.use('science')

# read in filtered data
coronasurveys_eng = pd.read_csv('data/filtered/coronasurveys-eng.csv')
coronasurveys_nir = pd.read_csv('data/filtered/coronasurveys-nir.csv')
coronasurveys_sct = pd.read_csv('data/filtered/coronasurveys-sct.csv')
coronasurveys_wls = pd.read_csv('data/filtered/coronasurveys-wls.csv')
coronasurveys_gb = pd.read_csv('data/filtered/coronasurveys-gb.csv')
ons_eng = pd.read_csv('data/filtered/ons-eng.csv')
ons_nir = pd.read_csv('data/filtered/ons-nir.csv')
ons_sct = pd.read_csv('data/filtered/ons-sct.csv')
ons_wls = pd.read_csv('data/filtered/ons-wls.csv')
ons_gb = pd.read_csv('data/filtered/ons-gb.csv')

# plot comparisons
def coronasurveys():
  '''All Coronasurveys regional data''' 
  plt.figure('Coronasurveys Data Plot', figsize=(8, 6))
  plt.plot(
    coronasurveys_eng['days'],
    coronasurveys_eng['p_cases'],
    label='England'
  )
  plt.fill_between(
    coronasurveys_eng['days'],
    coronasurveys_eng['p_cases_low'], # type: ignore
    coronasurveys_eng['p_cases_high'], # type: ignore
    alpha=0.25,
    label='England (error)'
  )
  plt.plot(
    coronasurveys_nir['days'],
    coronasurveys_nir['p_cases'],
    label='Northern Ireland'
  )
  plt.fill_between(
    coronasurveys_nir['days'],
    coronasurveys_nir['p_cases_low'], # type: ignore
    coronasurveys_nir['p_cases_high'], # type: ignore
    alpha=0.25,
    label='Northern Ireland (error)'
  )
  plt.plot(
    coronasurveys_sct['days'],
    coronasurveys_sct['p_cases'],
    label='Scotland'
  )
  plt.fill_between(
    coronasurveys_sct['days'],
    coronasurveys_sct['p_cases_low'], # type: ignore
    coronasurveys_sct['p_cases_high'], # type: ignore
    alpha=0.25,
    label='Scotland (error)'
  )
  plt.plot(
    coronasurveys_wls['days'],
    coronasurveys_wls['p_cases'],
    label='Wales'
  )
  plt.fill_between(
    coronasurveys_wls['days'],
    coronasurveys_wls['p_cases_low'], # type: ignore
    coronasurveys_wls['p_cases_high'], # type: ignore
    alpha=0.25,
    label='Wales (error)'
  )
  plt.plot(
    coronasurveys_gb['days'],
    coronasurveys_gb['p_active'],
    label='UK, active'
  )
  plt.fill_between(
    coronasurveys_gb['days'],
    coronasurveys_gb['p_active_low'], # type: ignore
    coronasurveys_gb['p_active_high'], # type: ignore
    alpha=0.25,
    label='UK, active (error)'
  )
  plt.title('Coronasurveys')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 100)
  plt.show()
def ons():
  '''All ONS regional data''' 
  plt.figure('ONS Data Plot', figsize=(8, 6))
  plt.plot(
    ons_eng['days'],
    ons_eng['p_infected'],
    label='England'
  )
  plt.fill_between(
    ons_eng['days'],
    ons_eng['p_infected_low'], # type: ignore
    ons_eng['p_infected_high'], # type: ignore
    alpha=0.25,
    label='England (error)'
  )
  plt.plot(
    ons_nir['days'],
    ons_nir['p_infected'],
    label='Northern Ireland'
  )
  plt.fill_between(
    ons_nir['days'],
    ons_nir['p_infected_low'], # type: ignore
    ons_nir['p_infected_high'], # type: ignore
    alpha=0.25,
    label='Northern Ireland (error)'
  )
  plt.plot(
    ons_sct['days'],
    ons_sct['p_infected'],
    label='Scotland'
  )
  plt.fill_between(
    ons_sct['days'],
    ons_sct['p_infected_low'], # type: ignore
    ons_sct['p_infected_high'], # type: ignore
    alpha=0.25,
    label='Scotland (error)'
  )
  plt.plot(
    ons_wls['days'],
    ons_wls['p_infected'],
    label='Wales'
  )
  plt.fill_between(
    ons_wls['days'],
    ons_wls['p_infected_low'], # type: ignore
    ons_wls['p_infected_high'], # type: ignore
    alpha=0.25,
    label='Wales (error)'
  )
  plt.plot(
    ons_gb['days'],
    ons_gb['p_infected'],
    label='UK'
  )
  plt.fill_between(
    ons_gb['days'],
    ons_gb['p_infected_low'], # type: ignore
    ons_gb['p_infected_high'], # type: ignore
    alpha=0.25,
    label='UK (error)'
  )
  plt.title('ONS')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 10)
  plt.show()
def eng():
  '''England plot''' 
  plt.figure('England Data Plot', figsize=(8, 6))
  plt.plot(
    coronasurveys_eng['days'],
    coronasurveys_eng['p_cases'],
    label='Coronasurveys'
  )
  plt.fill_between(
    coronasurveys_eng['days'],
    coronasurveys_eng['p_cases_low'], # type: ignore
    coronasurveys_eng['p_cases_high'], # type: ignore
    alpha=0.25,
    label='Coronasurveys (error)'
  )
  plt.plot(
    ons_eng['days'],
    ons_eng['p_infected'],
    label='ONS'
  )
  plt.fill_between(
    ons_eng['days'],
    ons_eng['p_infected_low'], # type: ignore
    ons_eng['p_infected_high'], # type: ignore
    alpha=0.25,
    label='ONS (error)'
  )
  plt.title('England')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 100)
  plt.show()
def nir():
  '''Northern Ireland plot''' 
  plt.figure('Northern Ireland Data Plot', figsize=(8, 6))
  plt.plot(
    coronasurveys_nir['days'],
    coronasurveys_nir['p_cases'],
    label='Coronasurveys'
  )
  plt.fill_between(
    coronasurveys_nir['days'],
    coronasurveys_nir['p_cases_low'], # type: ignore
    coronasurveys_nir['p_cases_high'], # type: ignore
    alpha=0.25,
    label='Coronasurveys (error)'
  )
  plt.plot(
    ons_nir['days'],
    ons_nir['p_infected'],
    label='ONS'
  )
  plt.fill_between(
    ons_nir['days'],
    ons_nir['p_infected_low'], # type: ignore
    ons_nir['p_infected_high'], # type: ignore
    alpha=0.25,
    label='ONS (error)'
  )
  plt.title('Northern Ireland')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 100)
  plt.show()
def sct():
  '''Scotland plot''' 
  plt.figure('Scotland Data Plot', figsize=(8, 6))
  plt.plot(
    coronasurveys_sct['days'],
    coronasurveys_sct['p_cases'],
    label='Coronasurveys'
  )
  plt.fill_between(
    coronasurveys_sct['days'],
    coronasurveys_sct['p_cases_low'], # type: ignore
    coronasurveys_sct['p_cases_high'], # type: ignore
    alpha=0.25,
    label='Coronasurveys (error)'
  )
  plt.plot(
    ons_sct['days'],
    ons_sct['p_infected'],
    label='ONS'
  )
  plt.fill_between(
    ons_sct['days'],
    ons_sct['p_infected_low'], # type: ignore
    ons_sct['p_infected_high'], # type: ignore
    alpha=0.25,
    label='ONS (error)'
  )
  plt.title('Scotland')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 100)
  plt.show()
def wls():
  '''Wales plot''' 
  plt.figure('Wales Data Plot', figsize=(8, 6))
  plt.plot(
    coronasurveys_wls['days'],
    coronasurveys_wls['p_cases'],
    label='Coronasurveys'
  )
  plt.fill_between(
    coronasurveys_wls['days'],
    coronasurveys_wls['p_cases_low'], # type: ignore
    coronasurveys_wls['p_cases_high'], # type: ignore
    alpha=0.25,
    label='Coronasurveys (error)'
  )
  plt.plot(
    ons_wls['days'],
    ons_wls['p_infected'],
    label='ONS'
  )
  plt.fill_between(
    ons_wls['days'],
    ons_wls['p_infected_low'], # type: ignore
    ons_wls['p_infected_high'], # type: ignore
    alpha=0.25,
    label='ONS (error)'
  )
  plt.title('Wales')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 100)
  plt.show()
def gb():
  '''UK active cases plot''' 
  plt.figure('UK Active Cases Data Plot', figsize=(8, 6))
  plt.plot(
    coronasurveys_gb['days'],
    coronasurveys_gb['p_active'],
    label='Coronasurveys'
  )
  plt.fill_between(
    coronasurveys_gb['days'],
    coronasurveys_gb['p_active_low'], # type: ignore
    coronasurveys_gb['p_active_high'], # type: ignore
    alpha=0.25,
    label='Coronasurveys (error)'
  )
  plt.plot(
    ons_gb['days'],
    ons_gb['p_infected'],
    label='ONS'
  )
  plt.fill_between(
    ons_gb['days'],
    ons_gb['p_infected_low'], # type: ignore
    ons_gb['p_infected_high'], # type: ignore
    alpha=0.25,
    label='ONS (error)'
  )
  plt.title('UK Active Cases')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 10)
  plt.show()

# show plots
print('Showing Coronasurveys data from all regions …')
coronasurveys()
print('Showing ONS data from all regions …')
ons()
print('\nRegional comparisons compare data across all sources.')
print('Coronasurveys data shows percentage of all recorded cases.')
print('ONS data shows percentage of active cases.\n')
print('Comparing England regional data …')
eng()
print('Comparing Northern Ireland regional data …')
nir()
print('Comparing Scotland regional data …')
sct()
print('Comparing Wales regional data …')
wls()
print('\nNow using only active case count data.')
print('Comparing UK data across all sources …')
gb()
