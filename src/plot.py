import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import sys
sys.path.insert(0, '../src')
sys.path.insert(0, '../data')

import clean
import aggregate


'''
Following functions plot the overall rate data
'''

# Retrieve mean rate for every year
def annual_rate(df):
    ser = df['Suicides_per_100K'].groupby(df.Year).mean()
    return ser

# Retieve overall average for all years
def annual_average(df):
    num = df['Suicides_per_100K'].sum() / df['Suicides_per_100K'].count()
    return num


def annual_rate_plot(df, title, xlabel, ylabel):
    ser = annual_rate(df)
    avg = annual_average(df)

    fig, ax = plt.subplots(figsize=(8,6))

    ax.plot(ser.index, ser.values, marker='o')

    ax.set_title(title, loc='left', fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12, fontweight='medium')
    ax.set_ylabel(ylabel, fontsize=12, fontweight='medium')

    ax.axhline(avg, linestyle='--', color='blue')

    return ax

'''
Global Map
'''



def world_map(df):

    fig = px.choropleth(df, locations="Country", locationmode='country names',
                    color="Suicides", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='sunset')

    return fig.show() 


if __name__ == '__main__':

    data = clean.read_file('data/master.csv')

    data = clean.clean_data(data, 2016, '5-14 years',
                            '05-14 years', ['country-year', 'HDI for year'])

    country_total = aggregate.column_total(data, 'Country')
    print(country_total)
    
