def andamento(funzione):
	def calcola_andamento(venduto,budget):
		print("Sto per chiamare la funzione 'scostamento'")
		scostamento = funzione(venduto,budget)
		print ("Il risultato della funzione :", scostamento)
		if scostamento >= 0:
			return 'Positivo'
		else:
			return 'Negativo'
	return calcola_andamento
@andamento
def scostamento(venduto, budget):
	return (venduto - budget) * 100 / budget
print scostamento
risultato = scostamento(2000,1000)
print(risultato)	