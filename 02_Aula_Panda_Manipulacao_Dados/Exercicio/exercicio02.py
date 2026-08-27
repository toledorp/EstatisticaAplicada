import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "WebCam", "HEadset"],
    "Categoria": ["Periférico", "Periférico", "Video", "Video", "Audio"],
    "Preco": [80, 120, 900, 250, 300],
    "Quantidade": [10, 8, 4, 6, 5]
}

df = pd.DataFrame(dados)

df["Valor_estoque"] = df["Preco"] * df["Quantidade"] 

print(df.iloc[df["Valor_estoque"].idxmax()]) #idxmax localiza o indice com o maior valor

print(df.iloc[df["Valor_estoque"].idxmin()])

print(df["Valor_estoque"].sum())