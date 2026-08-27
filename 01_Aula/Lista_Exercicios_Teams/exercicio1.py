import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "nome": ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Carlos", "Fernanda"],
    "idade": [18, 20, 19, 22, 21, 18, 23, 20],
}

df = pd.DataFrame(dados)

#Exibir o DataFrame
print(df)

#Mostar as cinco primeiras linhas do DataFrame
print(df.head())

#Exibir informações sobre o DataFrame
df.info()

#Exibir estatísticas descritivas do DataFrame
print(df.describe())