import numpy as np
import pandas as pd

dados = np.array([8, 10, 12])
dados_np = pd.array(dados)
dados_pd = pd.Series(dados)

# 1 Numpay (população por padrao)
dp_np = np.std(dados_np)
print("Desvio Padrão (Numpy): ", dp_np)

#2 Pandas (população por padrao)
dp_pd = dados_pd.std()
print("Desvio Padrão (Pandas): ", dp_pd)

