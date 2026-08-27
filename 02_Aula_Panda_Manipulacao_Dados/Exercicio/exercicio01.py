import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "WebCam", "HEadset"],
    "Categoria": ["Periférico", "Periférico", "Video", "Video", "Audio"],
    "Preco": [80, 120, 900, 250, 300],
    "Qauntidade": [10, 8, 4, 6, 5]
}

df = pd.DataFrame(dados)

print(df)
print(df.shape)
print(df.info())
print(df.describe())
print(df[["Produto", "Preco"]])
print(df.iloc[0:2])
print(df.iloc[df["Preco"].idxmax()]) #idxmax localiza o indice com o maior valor
print(df.iloc[df["Preco"].idxmin()]) #idxmax localiza o indice com o maior valor


