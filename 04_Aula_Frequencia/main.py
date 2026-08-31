import pandas as pd

notas = [
7, 8, 6, 9, 7,
5, 8, 7, 10, 6,
8, 9, 7, 5, 6,
8, 7, 9, 8, 10
]

serie = pd.Series(notas) #transforma o vetor em serie

print(serie.value_counts()) #frequencia absoluta

print(serie.value_counts().sort_index())

print(serie.value_counts().sort_values())
print(serie.value_counts(normalize=False)) # transforma para frequencia relatina (com True ) 


frequencia = serie.value_counts().sort_index()
frequencia_acumulada = frequencia.cumsum()
print(frequencia_acumulada)

## Criando dataFrame para\ tabela das frequencias
tabela = pd.DataFrame({
    "Frequencia_Absoluta": frequencia,
    "Frequencia_Relativa": frequencia / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada 
})

print(tabela)
