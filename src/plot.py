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
ons_eng = pd.read_csv('data/filtered/ons-eng.csv')
ons_nir = pd.read_csv('data/filtered/ons-nir.csv')
ons_sct = pd.read_csv('data/filtered/ons-sct.csv')
ons_wls = pd.read_csv('data/filtered/ons-wls.csv')

# plot comparisons
def coronasurveys():
  '''All Coronasurveys regional data''' 
  plt.figure('Coronasurveys Data Plot', figsize=(8, 6))
  plt.plot(
    coronasurveys_eng['days'],
    coronasurveys_eng['p_cases'],
    label='England'
  )
  plt.plot(
    coronasurveys_nir['days'],
    coronasurveys_nir['p_cases'],
    label='Northern Ireland'
  )
  plt.plot(
    coronasurveys_sct['days'],
    coronasurveys_sct['p_cases'],
    label='Scotland'
  )
  plt.plot(
    coronasurveys_wls['days'],
    coronasurveys_wls['p_cases'],
    label='Wales'
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
  plt.plot(
    ons_nir['days'],
    ons_nir['p_infected'],
    label='Northern Ireland'
  )
  plt.plot(
    ons_sct['days'],
    ons_sct['p_infected'],
    label='Scotland'
  )
  plt.plot(
    ons_wls['days'],
    ons_wls['p_infected'],
    label='Wales'
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
  plt.plot(
    ons_eng['days'],
    ons_eng['p_infected'],
    label='ONS'
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
  plt.plot(
    ons_nir['days'],
    ons_nir['p_infected'],
    label='ONS'
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
  plt.plot(
    ons_sct['days'],
    ons_sct['p_infected'],
    label='ONS'
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
  plt.plot(
    ons_wls['days'],
    ons_wls['p_infected'],
    label='ONS'
  )
  plt.title('Wales')
  plt.xlabel('Days since 2020/01/06')
  plt.ylabel('Percentage of cases')
  plt.legend(loc='upper left')
  plt.xlim(1000)
  plt.ylim(0, 100)
  plt.show()

# show plots
print('Showing Coronasurveys data from all regions …')
coronasurveys()
print('Showing ONS data from all regions …')
ons()
print('Regional comparisons compare data across all sources.')
print('Coronasurveys data shows percentage of all recorded cases.')
print('ONS data shows percentage of active cases.')
print('Comparing England regional data …')
eng()
print('Comparing Northern Ireland regional data …')
nir()
print('Comparing Scotland regional data …')
sct()
print('Comparing Wales regional data …')
wls()
