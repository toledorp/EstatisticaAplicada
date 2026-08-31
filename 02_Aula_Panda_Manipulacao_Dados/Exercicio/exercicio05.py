import pandas as pd

dados = {
    "Filme": [
        "Avatar", "Matrix", "Interestelar", "Vingadores", "Barbie",
        "O Poderoso Chefao", "Titanic", "Duna", "Spider-Man: Sem Volta para Casa", "Parasita"
    ],
    "Genero": [
        "Acao", "Sci-Fi", "Sci-Fi", "Acao", "Comedia",
        "Drama", "Romance", "Sci-Fi", "Acao", "Drama"
    ],
    "Ano": [
        2009, 1999, 2014, 2019, 2023,
        1972, 1997, 2021, 2021, 2019
    ],
    "Nota": [
        8.8, 8.7, 8.7, 8.4, 6.9,
        9.2, 7.9, 8.0, 8.2, 8.5
    ]
}

df = pd.DataFrame(dados)

# Mostre os filmes com nota maior que 8
print("\n--- Filmes com nota maior que 8 ---")
print (df[df["Nota"]>= 8])

# Ordene os filmes pela nota
print("\n--- Filmes ordenados pela nota  ---")
print(df.sort_values("Nota"))

# Encontre a maior e menor nota
print("\n--- Encontre a maior e menor nota ---")
print(df["Nota"].max())
print(df["Nota"].min())

# Calcule a média
print("\n--- Media ---")
print(df["Nota"].mean())