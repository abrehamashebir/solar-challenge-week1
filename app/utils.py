import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'datasets')

def load_data():
    df = pd.read_csv(os.path.join(DATA_DIR,'combined.csv'))
    
    return df

def get_summary_table(df):
    return (
        df.groupby('Country')[['GHI', 'DNI', 'DHI']]
        .agg(['mean', 'median', 'std'])
        .round(2)
    )
