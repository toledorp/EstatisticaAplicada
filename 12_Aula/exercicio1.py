import numpy as np
import pandas as pd
from scipy import stats

tempos = [
    145, 152, 148, 160, 155,
    149, 151, 147, 158, 153,
    146, 154, 150, 159, 148,
    152, 156, 149, 151, 157
]

#Criando DataFrame
dados = pd.DataFrame({"tempo_ms":tempos})

# Dado o vetor de tempos de resposta ao lado:
#• a) Calcule o tamanho da amostra (n).
n = len(dados)

#• b) Calcule a média amostral (x̄) e o desvio padrão amostral (s).
media =  dados["tempo_ms"].mean()
desvio = dados["tempo_ms"].std(ddof=1)

#• c) Calcule o Erro Padrão da Média (EP).
erro_padrao = desvio / np.sqrt(n)

#• d) Construa o IC de 95% usando scipy.stats.t.interval.
ic_inf, ic_sup = stats.t.interval(
    confidence = 0.95,
    df = n -1,
    loc = media,
    scale = erro_padrao
)

#• e) Imprima os resultados formatados com 2 casas decimais.
print(f"Média: {media:.2f} ms")
print(f"Desvio Padrão: {desvio:>2f} ms")
print(f"Erro Padrão: {erro_padrao:.2f} ms")
print(f"Limite Inferior: {ic_inf:.2f} ms")
print(f"Limite Superior: {ic_sup:.2f} ms")
print(f"ic 95% : [{ic_inf:.2f} ms ; {ic_sup:.2f} ms]")