import pandas as pd

dados = [10, 12, 15, 18, 20]

series = pd.Series(dados)


#a) Calcule manualmente a Média Aritmética (μ) dos valores.
print("Media aritimetica: {series.mean()}")

# b) Encontre a Amplitude (A) total dos valores.
print("Amplitude (A) : {series.max() - series.min()}")

# c) Calcule manualmente a Variância Populacional (σ²).
variancia = np.var(dados, ddof=0)
print("Variância Populacional (σ²):", variancia)

# d) Encontre o Desvio Padrão Populacional (σ).
desvio_padrao = np.std(dados, ddof=0)
print("Desvio Padrão Populacional (σ):", desvio_padrao)

# e) Crie um script em Python para validar todas as respostas.
print("\nValidação das respostas:")
print("Média (μ):", media)
print("Amplitude (A):", amplitude)
print("Variância Populacional (σ²):", variancia)
print("Desvio Padrão Populacional (σ):", desvio_padrao)
