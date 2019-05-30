import numpy as np
import pandas as pd
from sklearn import preprocessing

def gradientDescent(X,y,theta,alpha,m,numIterazioni):
    xTrans = X.transpose()
    ciclo_costi = []
    for i in range(0, numIterazioni):
        ral = 20000
        stima = ral + np.dot(X, theta)
        errore = stima - y
        costo = np.sum(errore ** 2)/(2 * m)
        ciclo_costi.append((i,costo))
        gradiente = np.dot(xTrans,errore)/m
        theta = theta - alpha * gradiente
    return ciclo_costi, theta

df = pd.read_csv('DataLab_Ral.csv')
linguaggi_enc = preprocessing.LabelEncoder()
istruzione_enc = preprocessing.LabelEncoder()
linguaggi = linguaggi_enc.fit(df['Linguaggio'])
istruzione = istruzione_enc.fit(df['Istruzione'])
df['Linguaggio'] = linguaggi.transform(df['Linguaggio'])
df['Istruzione'] = istruzione.transform(df['Istruzione'])
righe = df[['Linguaggio','Esperienza','Istruzione','Responsabile']].as_matrix()
y = df['RAL'].as_matrix()
m,n = np.shape(righe)
theta = np.ones(n)
alpha = 0.1
max_iter = 100
costi, pesi = gradientDescent(righe,y,theta,alpha,m,max_iter)
plot = pd.DataFrame(costi[:100], columns=['ciclo','costo']).plot()
fig = plot.get_figure()
fig.savefig('ciao.jpg')
