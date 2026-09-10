import pandas as pd

dados = pd.Series([8, 10, 12])

# 1 Variação Amostral (padrão do pandas - divide por n-1)
var_amostral = dados.var()
print("Variação Amostral: ", var_amostral)

# 2 Variação Populacional (divide por n)
var_populacao = dados.var(ddof=0)
print("Variação Populacional: ", var_populacao)

