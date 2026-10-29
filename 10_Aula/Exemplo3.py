import pandas as pd

#Conta a quantidade de ocorrencias de cada face (1 a 6) nos lançamentos do dado
frequencias = pd.Series(lancamentos).value_counts().sort_index()

print("Frequência de cada face do dado nos lançamentos:")
print(frequencias)