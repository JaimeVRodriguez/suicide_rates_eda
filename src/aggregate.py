import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import sys
sys.path.insert(0, '../src')
sys.path.insert(0, '../data')

import clean
import plot

'''
Get a total based on a particular column
'''
def column_total(df, column):
    total_df = df.groupby(column).sum().reset_index()

    return total_df
'''
Get a mean based on a particular column
'''
def coloumn_mean(df, column_list):
    mean_df = df.groupby(column_list).agg('mean').reset_index()

    return mean_df

'''
Apply a column filter to database based on a wanted value
'''
def column_filter(df, column, column_filter):
    df = df[df[column] == column_filter]

    return df

if __name__ == '__main__':

    data = clean.read_file('data/master.csv')
    data = clean.clean_data(data, 2016, '5-14 years',
                            '05-14 years', ['country-year', 'HDI for year'])

    country_total = column_total(data, 'Country')
    print(country_total)