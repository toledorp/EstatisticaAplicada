import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "filmes": ["Avatar", "Matrix", "Interestelar", "Vingadores", "Barbie"],
    "notas": [9.2, 9.5, 9.8, 8.9, 7.5]
}

df = pd.DataFrame(dados)

# Exiba o DataFrame.
print("Listando DataFrame")
print(df)

# Utilize head().
print("Utilizando head e exibindo a primeira linha")
print(df.head())

# Utilize describe().
print("Retornando as estatísticas descritivas do DataFrame")
print(df.describe())

# Construa um gráfico de barras.
print("Construido o grafico de barra")
plt.bar(df["filmes"], df["notas"])
plt.title("Grafico dos filmes x notas")
plt.xlabel("Filmes")
plt.ylabel("Notas")

plt.show()