import numpy as np
import pandas as pd
from scipy.stats import norm

#Fixar semente para reproducibilidade
np.random.seed(42)

# Gerar 1.000 tempos de resposta da API
#loc = média (200 ms), scale = desvio padrao (20 ms)
tempos = np.random.normal(
    loc = 200,
    scale = 20,
    size = 1000
) 

#Organizar em Dataframe pandas
dados = pd.DataFrame({'tempo_ms': tempos})

# Calculando estatísticas descritivas da amostra
media_amostral = dados['tempo_ms'].mean()
desvio_amostral = dados['tempo_ms'].std()

#Z = (X - média) / desvio

dados['zScore'] = (
    dados['tempo_ms'] - dados['tempo_ms'].mean()
) / dados['tempo_ms'].std()

print(dados.head(10))
