from matplotlib.dates import date2num
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import numpy as np

df = pd.DataFrame(
    {
        'data': ['01/05/2019','02/05/2019','03/05/2019','04/05/2019','05/05/2019','06/05/2019'],
        'valore': [2203.0,3260.0,2358.0,2342.0,2123.0,2321.5],
    },
    columns = ['data','valore']
)

df['data'] = df['data'].apply(datetime.strptime, args=("%d/%m/%Y",))
df['data'] = df['data'].apply(date2num)
print(df)
x = np.linspace(0,10,200)
y = np.cumsum(np.random.randn(200,3), axis=0)
etichette = ['storico {}'.format(i) for i in range(1,4)]
print(etichette)
sbn.set()
plt.legend(etichette,loc='upper left');
plt.plot(x,y)
plt.savefig('my-pic.jpg')
#
