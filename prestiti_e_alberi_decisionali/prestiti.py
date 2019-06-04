import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

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
plt.rcParams['figure.figsize'] = (10,10)
plt.style.use('ggplot')
plt.hist(df.estinto)
plt.savefig('prestiti.jpg')
plt.cla()
conteggio = df.livello.value_counts()
conteggio.plot.bar()
plt.savefig('prestiti1.jpg')
plt.cla()
conteggio = df.eta.value_counts()
conteggio.plot.bar()
plt.savefig('prestiti2.jpg')
plt.cla()
plt.scatter(df.eta,df.saldo,alpha=0.5)
plt.cla()
df.plot.scatter(
    x = 'eta',
    y = 'saldo',
    c = 'estinto',
    logx = True,
    logy = True,
    cmap = 'autumn'    
)
plt.savefig('prestiti4.jpg')
plt.cla()

