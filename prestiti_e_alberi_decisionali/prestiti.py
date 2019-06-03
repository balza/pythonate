import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.float_format', lambda x:'{0:.2f}'.format(x))
df = pd.read_csv("storico_prestiti.csv")
df.durata = df.durata.fillna(np.mean(df.durata))
pd.unique(df.durata)
df['livello'].unique()
#array(['B','A','C','D','E','F','G'], dtype=object)
df['tipologia'].unique()
#array(['Elettrodomestici', 'Autovettura', 'Elettronica', 'Altro'], dtype=object)
#
df_encoded = df.copy()
le_livello = LabelEncoder()
le_livello = le_livello.fit(df['livello'])
df_encoded.livello = le_livello.transform(df.livello)
le_tipologia = LabelEncoder()
le_tipologia = le_tipologia.fit(df['tipologia'])
df_encoded.tipologia = le_tipologia.transform(df.tipologia)
print(df_encoded.head)
