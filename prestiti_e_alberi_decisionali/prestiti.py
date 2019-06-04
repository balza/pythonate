import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import roc_curve,roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

def cross_validation(dataset, classificatore, k):
    X = dataset.iloc[:,:-1]  # tutto tranne l'ultima colonna
    y = dataset.iloc[:,-1]  # solo l'ultima colonna ("estinto")
    
    kf = StratifiedKFold(n_splits=k)
    
    valori_aree = []

    for train_index, test_index in kf.split(X,y):
        X_training = X.iloc[train_index]
        y_training = y.iloc[train_index]
        classificatore = classificatore.fit(X_training, y_training)
        previsioni = classificatore.predict_proba(X.iloc[test_index])[:,1]
        area = roc_auc_score(y.iloc[test_index],previsioni)
        valori_aree.append(area)
    
    return np.mean(valori_aree)

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
X_2 = df_encoded.loc[:,('eta','saldo')]
y = df_encoded.loc[:, 'estinto']
clf_dt = tree.DecisionTreeClassifier(max_depth=2)
clf_dt = clf_dt.fit(X_2, y)
print(clf_dt)
clf_dt_5 = tree.DecisionTreeClassifier(max_depth=5)
clf_dt_5 = clf_dt.fit(X_2, y)
esito_5_nodi = clf_dt_5.predict(X_2)
plt.hist(esito_5_nodi)
plt.savefig('prestiti5.jpg')
falsi_positivi, veri_positivi, _ = roc_curve(esito_5_nodi, df.estinto)
plt.plot(falsi_positivi, veri_positivi)
plt.savefig('prestiti6.jpg')
plt.cla()
score = roc_auc_score(esito_5_nodi, df.estinto)
print(score)
#
dt = tree.DecisionTreeClassifier(max_depth=5)
dataset = df_encoded[['eta','saldo','estinto']]
print(cross_validation(dataset,dt,5))
#
rfc = RandomForestClassifier(n_estimators=1000)
print(cross_validation(df_encoded, rfc, 5))

