import pandas as pd


dados = {
    "Produto": [
        "Mouse", "Teclado", "Monitor", "Webcam", "Headset",
        "Mousepad", "SSD 1TB", "Memoria RAM", "Cabo HDMI", "Hub USB"
    ],
    "Categoria": [
        "Perifericos", "Perifericos", "Hardware", "Perifericos", "Audio",
        "Acessorios", "Armazenamento", "Memoria", "Cabos", "Acessorios"
    ],
    "Preco": [
        49.90, 189.90, 899.00, 210.50, 149.99,
        35.00, 329.90, 299.00, 24.90, 89.90
    ],
    "Quantidade": [
        120, 85, 32, 45, 70,
        150, 60, 90, 110, 55
    ]
}

df = pd.DataFrame(dados)

#Criando nova coluna
df["Valor_Total"] = df["Preco"] * df["Quantidade"]

# Ordenando pelo preço
print(df.sort_values("Preco"))

# Encontre os produtos com preço > R$ 100,00
print(df[df["Preco"] <= 100])

# Encontre os produtos com quantidade < 10
print(df[df["Quantidade"] <= 100])

# Exercicio extra : encontre os procutos com preço >100 e quantidade < 10
print (df[(df["Preco"] >= 100) & (df["Quantidade"] >= 10)])