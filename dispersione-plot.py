import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.DataFrame(np.random.randn(100,2), columns=['X','y'])
print(df.head())
colori = np.random.rand(100)
dimensioni = np.random.rand(100) * 1000
plt.scatter(
    df['X'],
    df['y'],
    c=colori,
    s=dimensioni,
    alpha=0.3
)
plt.savefig('my-pic.jpg')
