import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

#Configuração de estilo dos graficos
plt.style.use('seaborn-v0_8-whitegrid')
print('Ambiente carregado com sucesso')

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
print(dados.head())



# Calculando estatísticas descritivas da amostra
media_amostral = dados['tempo_ms'].mean()
desvio_amostral = dados['tempo_ms'].std()
print(f'Média Amostral: {media_amostral:.2f}ms')
print(f'Desvio Padrão Amostral:{desvio_amostral:.2f} ms')
# Saída esperada no console:
# Média Amostral: 200.38 ms
# Desvio Padrão Amostral: 19.58 ms

x = np.linspace(tempos.min(), tempos.max(), 300)
y = norm.pdf(x, loc=media_amostral, scale=desvio_amostral)

plt.plot(x, y, color="blue", linewidth=2, label="curva normal")

# Plotando histograma dos tempos de resposta
plt.figure(figsize=(8, 4.5))
plt.hist(dados['tempo_ms'], bins=30, density=True, edgecolor='black', color='#B22222', alpha=0.7)
plt.axvline(dados['tempo_ms'].mean(),
color='black', linestyle='--', label='Média')
plt.xlabel('Tempo de resposta (ms)')
plt.ylabel('Frequência (Nº de Requisições)')
plt.title('Distribuição Amostral dos Tempos de Resposta')
plt.legend()
plt.tight_layout()
plt.show()