import numpy as np

#righe = df[['Linguaggio','Esperienza','Istruzione','Responsabile']].as_matrix()
#y = df['RAL'].as_matrix()
#m,n = np.shape(righe)
#theta = np.ones(n)
#stima = 20000 + np.dot(righe,theta)
#costo = stima - y


def GradientDescent(X,y,theta,alpha,m,numIterazioni):
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
        
