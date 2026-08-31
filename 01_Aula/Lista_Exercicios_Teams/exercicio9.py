import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Criando uma lista
produtos_lista = ["Mouse", "Teclado", "Monitor", "Webcam", "Headset", 
                   "Mousepad", "Hub USB", "Cabo HDMI", "SSD 1TB", "Memoria RAM"]

# 2. Criando o DataFrame com dados da loja
dados = {
    "Produto": produtos_lista,
    "Preco": np.round(np.random.uniform(3, 15, 10), 2),  # Quantidade entre e e 
    "Quantidade": np.random.randint(50, 900, 10) # Preços entre 50 e 900 
}

df = pd.DataFrame(dados)

# 3. Criando nova coluna 'Valor em Estoque' (Preço × Quantidade)
df["Valor em Estoque"] = df["Preco"] * df["Quantidade"]

print("=" * 80)
print("ANALISE DE ESTOQUE - LOJA DE INFORMATICA")
print("=" * 80)

# Exibindo a tabela completa
print("\n--- TABELA COMPLETA ---")
print(df.to_string())

# 4. Usando len() - Quantidade de produtos
print("\n" + "=" * 80)
print("1. QUANTIDADE DE PRODUTOS - len()")
print("=" * 80)
print(f"Total de produtos: {len(df)}")
print(f"Tamanho da lista: {len(produtos_lista)}")

# 5. Usando sum() - Soma total
print("\n" + "=" * 80)
print("2. SOMAS - sum()")
print("=" * 80)
print(f"Soma dos Precos: R$ {df['Preco'].sum():.2f}")
print(f"Soma das Quantidades: {df['Quantidade'].sum()} unidades")
print(f"Valor Total em Estoque: R$ {df['Valor em Estoque'].sum():.2f}")

# 6. Usando max() - Valor maximo
print("\n" + "=" * 80)
print("3. VALORES MAXIMOS - max()")
print("=" * 80)
print(f"Preco Maximo: R$ {df['Preco'].max():.2f}")
print(f"Quantidade Maxima em Estoque: {df['Quantidade'].max()} unidades")
print(f"Maior Valor em Estoque: R$ {df['Valor em Estoque'].max():.2f}")
print(f"Produto com maior valor: {df.loc[df['Valor em Estoque'].idxmax(), 'Produto']}")

# 7. Usando min() - Valor mínimo
print("\n" + "=" * 80)
print("4. VALORES MINIMOS - min()")
print("=" * 80)
print(f"Preco Minimo: R$ {df['Preco'].min():.2f}")
print(f"Quantidade Minima em Estoque: {df['Quantidade'].min()} unidades")
print(f"Menor Valor em Estoque: R$ {df['Valor em Estoque'].min():.2f}")
print(f"Produto com menor valor: {df.loc[df['Valor em Estoque'].idxmin(), 'Produto']}")

# 8. Usando head() - Primeiras linhas
print("\n" + "=" * 80)
print("5. PRIMEIRAS 5 LINHAS - head()")
print("=" * 80)
print(df.head())

# 9. Usando info() - Informações do DataFrame
print("\n" + "=" * 80)
print("6. INFORMAÇÕES DO DATAFRAME - info()")
print("=" * 80)
print(df.info())

# 10. Usando describe() - Estatisticas descritivas
print("\n" + "=" * 80)
print("7. ESTATiSTICAS DESCRITIVAS - describe()")
print("=" * 80)
print(df.describe())

# 11. Grafico de barras - Valor em Estoque por Produto
print("\n" + "=" * 80)
print("8. GERANDO GRaFICO DE BARRAS")
print("=" * 80)
plt.figure(figsize=(14, 6))
plt.bar(df["Produto"], df["Valor em Estoque"], color="steelblue", edgecolor="black")
plt.title("Valor em Estoque por Produto", fontsize=16, fontweight="bold")
plt.xlabel("Produto", fontsize=12)
plt.ylabel("Valor em Estoque (R$)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# Resumo final
print("\n" + "=" * 80)
print("RESUMO EXECUTIVO")
print("=" * 80)
print(f"Total de Produtos: {len(df)}")
print(f"Valor Total em Estoque: R$ {df['Valor em Estoque'].sum():,.2f}")
print(f"Preco Medio: R$ {df['Preco'].mean():.2f}")
print(f"Quantidade Media em Estoque: {df['Quantidade'].mean():.2f} unidades")
