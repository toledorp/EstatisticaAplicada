## variavel categoria

import pandas as pd

tabela = pd.read_csv('dados.csv')

serie = tabela['estado']


frequencia_absoluta = serie.value_counts()
frequencia_acumulada = frequencia_absoluta.cumsum()


## Criando dataFrame para\ tabela das frequencias
tabela = pd.DataFrame({
    "Frequencia_Absoluta": frequencia_absoluta,
    "Frequencia_Relativa": frequencia_absoluta / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada 
})

print(tabela)
