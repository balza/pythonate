import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(
    {
        'eta': [17,18,19,20,21],
        'm': [55,52,58,42,123],
        'f': [35,45,58,25,123]
    },
    columns = ['eta','m','f']
)

print(df)
plt.bar(
    range(len(df)), 
    df['m'],
    align='center',
    color='b',
    label='M'
)
plt.bar(
    range(len(df)), 
    df['f'],
    align='center',
    color='r',
    label='F',
    bottom=df['m']
)
plt.xticks(range(len(df)),df['eta'],rotation='vertical')
plt.legend()
plt.savefig('my-pic.jpg')
