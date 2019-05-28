import pandas as pd

df = pd.read_csv("dow_jones_index/dow_jones_index.data")
df['date'] = pd.to_datetime(df['date'])
def converti_valori_monetari(stringa):
    valore = stringa.replace('$','')
    return float(valore)
colonne_da_convertire = ('open','high','low','close','next_weeks_open','next_weeks_close')
for colonna in colonne_da_convertire:
    df[colonna] = df[colonna].apply(converti_valori_monetari)
print(df.head())
print(df.describe())
print(df.iloc[5:11])
