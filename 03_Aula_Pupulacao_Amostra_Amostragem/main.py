# import random

# alunos = ["Rogerio", "Ricado", "Shimada", "Caio", "Camila", "vitor", "Giovana", "Miguel", "Renan", "Carlos", "Ana", "Sthevens", "Guilherme", "Raisa", "Matheus", "Felipe", "Endrew", "Arthur", "Gabriela", "Pedro"]

# random.seed(15)

# amostra = random.sample(alunos, 3)

# print(amostra)


import pandas as pd

df = pd.read_csv("dados.csv")

amostra = df.sample(n=100)

medPopulacao = df["idade"].mean()
print (f"média da população: {medPopulacao}")

# print(df.shape)

# print(df.head())

# print (amostra.head)

medAmostra = amostra["idade"].mean()
print (f"Média da população: {df["idade"].mean()}")


print (f"Média da amostra: {amostra["idade"].mean()}")

print 