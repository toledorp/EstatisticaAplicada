import pandas as pd
import matplotlib.pyplot as plt


dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana"],
    "Idade": [18, 20, 19, 22],
}

df = pd.DataFrame(dados)

#Exibir o dataframe
print(df)

#Contar os registro do fataFrame
print(len(df)) #1ª maneira
print(df.shape) #2ª maneira

#Visualizar as informações
df.info()


