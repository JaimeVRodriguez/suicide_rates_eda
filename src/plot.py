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
# Following functions plot the overall rate data
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
Creates a global heat map for total suicides
'''

def world_map(df):

    fig = px.choropleth(df, locations="Country", locationmode='country names',
                    color="Suicides", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale='sunset')

    return fig.show() 

'''
Line Plot
'''

def line_plot(df, xaxis, yaxis, title, xlabel, ylabel, hue):

    fig, ax = plt.subplots(figsize=(8,6))

    sns.lineplot(x=xaxis, y=yaxis, hue=hue, ax=ax, data=df, marker='o')
    ax.set_title(title, loc='left', fontsize=18, fontweight='bold')

    ax.set_xlabel(xlabel, fontsize=12, fontweight='medium')
    ax.set_ylabel(ylabel, fontsize=12, fontweight='medium')
    
    return ax

'''
Double plot (specifically for annual rate by gender)
'''

def two_plot(df1, ax1_title, df2, ax2_title, title, xlabel, ylabel, color):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))

    fig.suptitle(title, horizontalalignment='right', fontsize=18, fontweight='bold')

    sns.lineplot(x='Year', y='Suicides_per_100K', ax=ax1, data=df1, color=color[1])
    ax1.set_title(ax1_title)
    ax1.set_xlabel(xlabel, fontsize=12, fontweight='medium')
    ax1.set_ylabel(ylabel, fontsize=12, fontweight='medium')
    ax1.set_yticks([15,19,23,27])

    sns.lineplot(x='Year', y='Suicides_per_100K', ax=ax2, data=df2, color=color[0] )
    ax2.set_title(ax2_title)
    ax2.set_xlabel(xlabel, fontsize=12, fontweight='medium')
    ax2.set_ylabel(ylabel, fontsize=12, fontweight='medium')

    fig.tight_layout()

'''
Bar plot comparing two categories(columns)
'''
def bar_plot(df, column_one, column_two, color):
    fig, ax = plt.subplots(figsize=(8,6))
    ax.ticklabel_format(useOffset=False, style='plain', axis='y')

    ax.bar(df[column_one], df[column_two], color=color)

    ax.set_title('Total Suicided by Age', loc='left', fontsize=18, fontweight='bold')
    ax.set_xlabel('Age Group', fontsize=12, fontweight='medium')
    ax.set_ylabel('Suicides', fontsize=12, fontweight='medium')



if __name__ == '__main__':
    plt.style.use('ggplot')
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    data = clean.read_file('data/master.csv')

    data = clean.clean_data(data, 2016, '5-14 years',
                            '05-14 years', ['country-year', 'HDI for year'])

    # males = aggregate.column_filter(data, 'Sex', 'male')
    # females = aggregate.column_filter(data, 'Sex', 'female')

    # wo_plot(males, 'Males', females, 'Females', 'Suicide Rate (by Gender)', 'Year', 'Suicides per 100K', colors)
    