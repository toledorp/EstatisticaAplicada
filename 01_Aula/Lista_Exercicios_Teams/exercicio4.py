import pandas as pd
import matplotlib.pyplot as plt


dados = {
    "produto": ["Arroz", "Feijão", "Cafe", "Açucar", "Leite", "Óleo", "Macarrão"],
    "preco": [32, 11, 24, 6, 8, 9, 7]
}

df = pd.DataFrame(dados)

# Construa um gráfico de barras.
plt.bar(df["produto"], df["preco"])

# Altere o título.
plt.title("Grafico Produtos x Preço")

# Nomeie os eixos X e Y.
plt.xlabel("Produto")
plt.ylabel("Preço")

plt.show()