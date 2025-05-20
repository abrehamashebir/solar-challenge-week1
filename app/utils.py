import pandas as pd

def load_data():
    benin = pd.read_csv('data/benin_clean.csv')
    sierra_leone = pd.read_csv('data/sierraleone_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')

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
