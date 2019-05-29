import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(
    {
        'tipo': [
            'Sintassi',
            'PEP8',
            'Bug',
            'Performance',
            'Funzioni lughe',
            'Codice non documentato',
            'Naming'
        ],
        'count': [0,2,2,1,2,3,3]
    },
    columns = ['tipo','count']
)

print(df)
plt.bar(
    range(len(df)), 
    df['count'],
    align='center'
)
plt.xticks(range(len(df)),df['tipo'],rotation='vertical')
plt.savefig('my-pic.jpg')
