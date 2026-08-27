#nosso primeiro dataFrame

import pandas as pd

dados = {
    "Aluno": ["Rogério", "Mathues", "Camila", "Geovana"],
    "Nota":[8, 5, 9, 6]
}

df = pd.DataFrame(dados)

# df.info() = retorna informações sobre o DataFrame, como o número de entradas, colunas, tipos de dados e memória utilizada.
# print(df.describe()) = retorna estatísticas descritivas do DataFrame, como média, desvio padrão, valores mínimo e máximo, entre outros.
# print(df.head()) =  retorna as primeiras linhas do DataFrame

df.info()
print(df.describe()) 
print(df.head())