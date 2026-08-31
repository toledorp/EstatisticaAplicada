import pandas as pd

dados = {
    "Alunos": ["Ana", "Fernanda", "Joao", "Carlos", "Ricardo", "Camila", "Angela", "Sergio", "Fabio", "Jose"],
    "Idade": [18, 22, 30, 34, 24, 26, 19, 42, 56, 37],
    "Nota": [6.5, 7, 8.2, 9.1, 6, 4, 8, 7, 7, 5.5]
}

df = pd.DataFrame(dados)

print("=" * 35)
print("ANALISE DE DADOS - FATE / REGISTRO")
print("=" * 35)

# calcule a média;
print("\n--- Calculos das Medias ---")
print("\n--- Idade ---")
print(df["Idade"].mean())
print("\n--- Nota ---")
print(df["Nota"].mean())

# encontre a maior nota;
print("\n--- Maior Nota ---")
print(df["Nota"].max())

# encontre a menor nota;
print("\n--- Menor Nota ---")
print(df["Nota"].min())

# ordene pela nota;
print("\n--- Ordenado por Nota ---")
print(df.sort_values("Nota"))


# mostre apenas alunos com nota ≥ 7
print("\n--- Notas acima de 7 ---")
print(df[df["Nota"] >= 7])
