import pandas as pd

df = pd.read_csv("../dados.csv")

amostra = df.sample(n=100)

mdGasto = df["valor_total_compras"].mean()
print(f"O Gasto médio da população : {mdGasto}")

amostra10 = df.sample(n=10, random_state=42)
print(f"Amostra com 5 clientes: {amostra10}")

gastoMedioAmostra = amostra["valor_total_compras"].mean()
print(f"O gasto médio da amostra: {gastoMedioAmostra}")

amostra30 = df.sample(n=30, random_state=42)
print(f"Amostra com 5 clientes: {amostra30}")

# Compare as duas médias
print(amostra30 - amostra10)
