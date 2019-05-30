import pandas as pd

df = pd.read_csv('DataLab_Ral.csv')
raggruppamenti = [
    'Linguaggio',
    'Responsabile',
    'Istruzione',
    'Esperienza'
]
agg = df.groupby(raggruppamenti).agg('mean')
df_agg = agg.reset_index()
df_agg[df_agg['Linguaggio'] == 'Python']
df.head()
print(df_agg)


def stimami_la_ral(linguaggio, is_manager, istruzione, anni_esp):
    ral = 20000
    ral += ral * pesi_linguaggio[linguaggio]
    ral += ral * pesi_istruzione[istruzione]
    ral += ral * pesi_anni[anni_esp]
    if is_manager:
        ral += ral * peso_manager
    return ral

pesi_linguaggio = {
    'Python': 0.05,
    'Javascript': 0.01,
    'Java': 0.03,
    'R': 0.07,
    'C#': 0.02,
    'Objective-C/Swift': 0.03,
    'SQL': 0.02,
    'COBOL': 0.04
}

pesi_istruzione = {
    'Diploma': 0,
    'Laurea Triennale': 0.02,
    'Laurea Magistrale': 0.03,
    'Dottorato': 0.05
}

def pesi_anni(anni_esperienza):
    if anni_esperienza > 8:
        return 1
    elif 6 < anni_esperienza <=8:
        return 0.7
    elif 4 < anni_esperienza <=6:
        return 0.5
    elif 1 < anni_esperienza <=4:
        return 0.25
    else:
        return 0

pesi_anni = {anni: pesi_anni(anni) for anni in range (1,41)}
peso_manager = 0.5

ral = stimami_la_ral('Python', 0, 'Dottorato', 2)
print(ral)

