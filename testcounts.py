#Author: Da'Mya Campbell (damycamp@cisco.com)
#File: testcounts.py
#Date: May 2018 (c) Cisco Systems
#Description: Calculates the total count of testcases per branch per family.

import pandas as pd
from datetime import datetime

raw_data = pd.read_csv('up2018.csv', usecols=['Date','Family','Branch','TestCase'], index_col = 0)
raw_data.to_csv('newup2018.csv')
new_raw_data = pd.read_csv('newup2018.csv')
# convert dates into datetime objects and week numbers (weekstart equals Monday)
new_raw_data['Date'] = pd.to_datetime(new_raw_data['Date']).dt.week
new_raw_data.sort_values(['Date'], inplace = True)
# create dataframe
df = pd.DataFrame(new_raw_data, columns = ['Family','Branch','TestCase','Date'])
total count pivot table
totalcount_table = pd.pivot_table(df, index = ['Family','Branch'], values = ['TestCase'], columns = ['Date'], aggfunc = 'count', fill_value = 0).astype(int).
# distinct count pivot table
distinctcount_table = pd.pivot_table(df, index = ['Family','Branch'], values = ['TestCase'], columns = ['Date'], aggfunc = lambda x: len(x.unique()),fill_value = 0).astype(int)
# display data from 2018 only
totalcount_table = totalcount_table.iloc[:,:21]
distinctcount_table = distinctcount_table.iloc[:,:21]
print(totalcount_table)