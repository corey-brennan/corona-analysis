# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:07:22 2020

@author: Corey
"""
import csv
import glob
import os
from bokeh.plotting import figure, output_file, show
import pandas as pd
from pandas import DataFrame
import numpy as np  
import matplotlib
 

#%%

## read all csv files, covid daily reports frm April 12th to Augest 20th

#os.chdir("C:\\Users\\Robin\\Documents\\Gatech\\COVID-19-master\\COVID-19-master\\csse_covid_19_data\\csse_covid_19_daily_reports_us")

#extension = "csv"
os.chdir("E:/corona-analysis")
print(os.getcwd())
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
combined_csv = pd.read_csv (r'combined_csv.csv')

States = ["New York", "Texas", "Massachusetts"]
df = combined_csv[combined_csv.Province_State.isin(States)]
ny_df = df[df.Province_State.str.contains("New York")]

tx_df = df[df.Province_State.str.contains("Texas")]

ma_df = df[df.Province_State.str.contains("Massachusetts")]

df[['Date', 'Time']] = df.Last_Update.str.split(expand=True)

df['Date'] = pd.to_datetime(df['Date'])

#%%
df.set_index('Date', inplace=True)
df.groupby('Province_State')['Confirmed'].plot(legend=True)