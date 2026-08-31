import pandas as pd

# 1. Criar a base de dados com 15 produtos
produtos = {
    "Produto": [
        "Mouse", "Teclado", "Monitor", "Webcam", "Headset",
        "Mousepad", "SSD 1TB", "Memoria RAM", "Cabo HDMI", "Hub USB",
        "Impressora", "Caixa de Som", "Placa de Video", "Fonte", "Pendrive"
    ],
    "Categoria": [
        "Perifericos", "Perifericos", "Hardware", "Perifericos", "Audio",
        "Acessorios", "Armazenamento", "Memoria", "Cabos", "Acessorios",
        "Impressao", "Audio", "Hardware", "Hardware", "Armazenamento"
    ],
    "Preco": [
        49.90, 189.90, 899.00, 210.50, 149.99,
        35.00, 329.90, 299.00, 24.90, 89.90,
        459.00, 180.00, 2299.90, 320.00, 58.50
    ],
    "Quantidade": [
        15, 12, 7, 9, 10,
        20, 6, 8, 25, 11,
        4, 5, 3, 2, 18
    ]
}

# 2. Criar o DataFrame
# 3. Criar a coluna Valor_Estoque

df = pd.DataFrame(produtos)
df["Valor_Estoque"] = df["Preco"] * df["Quantidade"]

# 4. Mostrar os 5 primeiros registros
print("\n===== 5 PRIMEIROS REGISTROS =====")
print(df.head())

# 5. Mostrar as informações da tabela
print("\n===== INFORMACOES DA TABELA =====")
print(df.info())

# 6. Calcular o preço médio
print("\n===== PRECO MEDIO =====")
print(f"Preco medio: R$ {df['Preco'].mean():.2f}")

# 7. Encontrar o produto mais caro
produto_mais_caro = df.loc[df["Preco"].idxmax()]
print("\n===== PRODUTO MAIS CARO =====")
print(f"Produto: {produto_mais_caro['Produto']}")
print(f"Preco: R$ {produto_mais_caro['Preco']:.2f}")

# 8. Encontrar o produto mais barato
produto_mais_barato = df.loc[df["Preco"].idxmin()]
print("\n===== PRODUTO MAIS BARATO =====")
print(f"Produto: {produto_mais_barato['Produto']}")
print(f"Preco: R$ {produto_mais_barato['Preco']:.2f}")

# 9. Ordenar pelo valor do estoque
print("\n===== ORDENADO POR VALOR DO ESTOQUE =====")
print(df.sort_values("Valor_Estoque", ascending=False))

# 10. Mostrar produtos com estoque inferior a 5 unidades
print("\n===== PRODUTOS COM ESTOQUE INFERIOR A 5 =====")
print(df[df["Quantidade"] < 5])

# 11. Calcular o valor total do estoque
print("\n===== VALOR TOTAL DO ESTOQUE =====")
print(f"Valor total: R$ {df['Valor_Estoque'].sum():.2f}")
