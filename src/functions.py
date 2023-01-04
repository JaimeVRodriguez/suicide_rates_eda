import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Takes in csv file and outputs a dataframe for use throughout project.
def read_file(csv_file):

    df = pd.read_csv(csv_file)
    return df

# Rename columns


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
