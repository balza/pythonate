import matplotlib.pyplot as plt
import numpy as np

def funzione_retta(x):
    return 3*x + 1
X = np.arange(10)
y = funzione_retta(X)
plt.xlim(-1,11)
plt.ylim(-1,50)
plt.plot(X,y, color='#ff9900',linestyle='--', label='y= 3*x + 1')
plt.plot(X, X*X, label='y=x^2')
plt.legend()
plt.savefig('my-pic.jpg')
