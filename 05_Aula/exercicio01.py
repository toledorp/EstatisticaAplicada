import pandas as pd

notas = pd.Series([7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10])
ordenadas = notas.sort_values()

print("Notas ordenadas: ")
print(ordenadas)
print("Média das notas: ", notas.mean())
print("Mediana das notas: ", notas.median())
print("Moda das notas: ")
print(notas.mode())
print("Menor nota: ", notas.min())
print("Maior nota: ", notas.max())
