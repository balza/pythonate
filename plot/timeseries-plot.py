from matplotlib.dates import date2num
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

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
plt.plot_date(x=df['data'], y=df['valore'], fmt='r-')
plt.savefig('my-pic.jpg')
