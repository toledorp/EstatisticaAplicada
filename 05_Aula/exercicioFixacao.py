import pandas as pd

tempos = pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])

#Imprimindo a média dos tempos
print("Média dos tempos: ", tempos.mean())
print("Média dos tempos arredondada: ", round(tempos.mean(), 2))
print("Mediana dos tempos: ", tempos.median())
print("Moda dos tempos: ", tempos.mode())
print("Desvio padrão dos tempos: ", tempos.std())
print("O valor mínimo dos tempos: ", tempos.min())
print("O valor máximo dos tempos: ", tempos.max())
print("O valor que melhor representa os tempos e a mediana, que é: ", tempos.median())