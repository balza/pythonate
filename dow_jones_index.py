import numpy as np

with open("dow_jones_index/dow_jones_index.data") as f:
    data = f.readlines()
    data = [riga.replace("\n","") for riga in data]
dataset = np.array([riga.split(",") for riga in data])
print(dataset)
    
