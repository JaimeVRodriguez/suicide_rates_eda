import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

'''
Following functions cleans the data into its final form.
Final version will be output in the clean_data function
'''

# Takes in csv file and outputs a dataframe for use throughout project.
def read_file(csv_file):

    df = pd.read_csv(csv_file)
    return df

# Remove data from 2016 (not enough data)
def remove_year(df, year):
    df = df[df.year != year]

    return df

# Replace elements inside column in order to utilize better
def replace_column_items(df, column_item, replacement):
    df = df.replace({column_item: replacement})

    return df

# Countries that had less than 3 years of data
def less_than_three_years(df):
    grouped = df.groupby('country').count()
    country_list = grouped[grouped.year <= 36]
    return country_list.index

# # Remove countries that had less than 3 years of data
def remove_countries(df):
    country_filter = less_than_three_years(df)

    df = df[~df['country'].isin(country_filter)]
    return df

# Drop unneeded columns
def remove_columns(df, column_list):
    df = df.drop(columns=column_list)

    return df

# Rename columns for human readability
def rename(df):
    dict = {
        'country': 'Country',
        'year': 'Year',
        'sex': 'Sex',
        'age': 'Age',
        'suicides_no': 'Suicides',
        'population': 'Population',
        'suicides/100k pop': 'Suicides_per_100K',
        ' gdp_for_year ($) ': 'Annual_GDP',
        'gdp_per_capita ($)': 'GDP_per_Capita',
        'generation': 'Generation'
    }

    df.rename(columns=dict,
              inplace=True)

    return df


def clean_data(df, year, column_item, replacement, column_list):
    df = remove_year(df, year)

    df = replace_column_items(df, column_item, replacement)

    df = remove_countries(df)

    df = remove_columns(df, column_list)

    df = rename(df)

    return df
    
if __name__ == '__main__':

    initial_data = read_file('data/master.csv')

    # initial_data = remove_year(initial_data, 2016)

    # initial_data = replace_column_items(
    #     initial_data, '5-14 years', '05-14 years')

    # remove_list = less_than_three_years(initial_data)

    # initial_data = remove_countries(initial_data, removal_list)

    # initial_data = remove_columns(
    #     initial_data, ['country-year', 'HDI for year'])

    # initial_data = rename(initial_data)

    final_data = clean_data(initial_data, 2016, '5-14 years',
                            '05-14 years', ['country-year', 'HDI for year'])
    print(final_data)
