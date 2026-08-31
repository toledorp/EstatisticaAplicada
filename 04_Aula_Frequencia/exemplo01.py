import pandas as pd

tabela = pd.read_csv('dados.csv')

# print(tabela.head())

serie = tabela["idade"]
print(serie.value_counts())
print(serie.value_counts().sort_index())
print(serie.value_counts().sort_values())

print(serie.value_counts(normalize=True) * 100) ## frequenciaRelativa

frequencia_absoluta = serie.value_counts().sort_index()
frequencia_acumulada = frequencia_absoluta.cumsum()
print(frequencia_acumulada)

## Criando dataFrame para\ tabela das frequencias
tabela = pd.DataFrame({
    "Frequencia_Absoluta": frequencia_absoluta,
    "Frequencia_Relativa": frequencia_absoluta / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada 
})

print(tabela)
