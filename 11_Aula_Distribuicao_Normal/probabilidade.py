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

def calcularScoreZ(x, media, dp):
    return (x - media_amostral) / desvio_amostral

z = calcularScoreZ(300, 200, 20)
print(f"Escore Z par x=300: {z}")

probabilidade_X_abaixo_220 = norm.cdf(220, loc=200, scale=20)
print(f"Probabilidade de X<220 é : {probabilidade_X_abaixo_220} ms")
print(f"Probabilidade de X<220 é : {probabilidade_X_abaixo_220 * 100} ms")

probabilidade_x_acima_240 = norm.sf(240, loc=200, scale=20)
print(f"Probabilidade de X<240 é : {probabilidade_x_acima_240} ms")
print(f"Probabilidade de X<240 é : {probabilidade_x_acima_240 * 100:.2f} ms")

#P(180 < X < 220)
cdf_Superior = norm.cdf(220, loc=200, scale=20)
cdf_Inferior = norm.cdf(180, loc=200, scale=20)
prob_intervalor = cdf_Superior - cdf_Inferior
print(f"P(180 < X < 220): {prob_intervalor:.4f}")
print(f"P(180 < X < 220): {prob_intervalor * 100:.4f} %")

