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


def column_total(df, column):
    total_df = df.groupby(column).sum().reset_index()

    return total_df

def coloumn_mean(df, column_list):
    mean_df = df.groupby(column_list).agg('mean').reset_index()

    return mean_df

def column_filter(df, column, column_filter):
    df = df[df[column] == column_filter]

    return df