import pandas as pd

tempo = pd.Series([
    120, 125, 121, 119, 123, 122
])

#Media
print("Média: ", tempo.mean())

#Amplitude
print("Amplitude: ", tempo.max() - tempo.min()) 

#Nota: var() e std() no Pandas usam ddof=1 por padrão, ou seja, calcula a variância e desvio padrão amostral.

print("Variação Amostral: ", tempo.var())
print("Desvio Padrão Amostral: ", tempo.std())
print("Desvio Padrão Populacional: ", tempo.std(ddof=0))
