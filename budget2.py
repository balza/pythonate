def versus_budget(budget):
    def scostamento (venduto):
        return (venduto - budget) * 100 / budget
    return scostamento
scostamento = versus_budget(10000)
negozi = {
    'Reggio Emilia': 10230,
    'Milano': 10500,
    'Torino': 9750,
    'Roma': 8030
}
for negozio, fatturato in negozi.items():
    print(negozio,'{}%'.format(scostamento(fatturato)))
