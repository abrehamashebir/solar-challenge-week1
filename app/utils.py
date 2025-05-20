import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
import os
print(os.path.join(DATA_DIR, 'benin_clean.csv'))
print(os.path.exists(os.path.join(DATA_DIR, 'benin_clean.csv')))

def load_data():
    benin = pd.read_csv(os.path.join(DATA_DIR,'benin_clean.csv'))
    sierra_leone = pd.read_csv(os.path.join(DATA_DIR,'sierraleone_clean.csv'))
    togo = pd.read_csv(os.path.join(DATA_DIR,'togo_clean.csv'))

    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    df = pd.concat([benin, sierra_leone, togo], ignore_index=True)
    return df

def get_summary_table(df):
    return (
        df.groupby('Country')[['GHI', 'DNI', 'DHI']]
        .agg(['mean', 'median', 'std'])
        .round(2)
    )
