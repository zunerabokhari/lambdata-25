import pandas as pd
def null_count(df):
    return df.isna().sum().sum()
 
def split_dates(df):
    df[['month', 'day', 'year']] = df['date'].str.split('/', expand=True)
    return df
