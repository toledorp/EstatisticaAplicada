import pandas as pd

salario = pd.Series([2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700,
2800, 20000])
print("Média do salário: ", salario.mean())
print("Mediana do salário: ", salario.median())

maior_frequencia = salario.value_counts().max()

if maior_frequencia > 1:
    print("Moda dos salario:", salario.mode().tolist())
else:
    print("Não há moda, pois nenhum tempo se repete.")

print("Menor salário: ", salario.min())
print("Maior salário: ", salario.max())
