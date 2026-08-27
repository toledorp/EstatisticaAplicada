# import pandas as pd

# dados = {
#     "Nome":["Ana", "Carlos", "João", "Felipe", "Marcos", "José"],
#     "Idade":[20, 25, 63, 10, 58, 25],
#     "Notas":[10, 5, 9, 8, 7, 3]
# }


# df = pd.DataFrame(dados)

# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.head())
# print(df.Nome)
# print(type(df["Idade"]))
# print(df[["Nome", "Notas"]])
# print(df.iloc[[0,3]])
# print(df.iloc[4, 2])
# print(df["Notas"].mean())
# print(df["Notas"].max())
# print(df["Notas"].min())
# print(df["Notas"].sum())

# incluir uma coluna
# df["Nota_final"] = df["Notas"] + 1.3

# print(df)

#Criando uma coluna Calculada

# import pandas as pd

# dados ={
#     "Produto": ["Mouse", "Teclado", "Monitor", "Gabinete"],
#     "Preco":[80, 50, 800, 250],
#     "Quantidade":[10, 50, 15, 25]
# }

# df = pd.DataFrame(dados)

# #incluir um nova coluna
# df["Valor_Total"] = df["Preco"] * df["Quantidade"]

# print(df)

#Metodo de ordenar dados
# df.sort_values("Produto")

# print(df.sort_values("Valor_Total"))

# print(df["Quantidade"] < 20)
# print(df[df["Quantidade"] < 20])
# print(df[df["Quantidade"] <= 15]
# print(df[(df["Quantidade"] <20) & (df["Preco"] < 300)])

#Importando arquivo CSV

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("dados.csv")
# print(df.info())
# print(df.head())
# print(df.describe())

# plt.figure(figsize=(10, 6)) #define o tamanho da figura 
# plt.bar(df["nota"], df["idade"]) #define o tipo de grafico e os dados que serao utilizados
# plt.title("Gráfico de notas por idade") #define o titulo do grafico 
# plt.show() #exibe o grafico
