import pandas as pd
import matplotlib.pyplot as plt


dados = {
    "produto": ["Arroz", "Feijão", "Macarrão", "Açúcar"],
    "preço": [5.50, 7.20, 4.30, 3.80],
    "quantidade": [10, 15, 8, 12]

}

df = pd.DataFrame(dados)

#Grafico1
# plt.bar(df["produto"], df["preço"]) #define o tipo de grafico e os dados que serao utilizados
# plt.title("Gráfico de Preços dos Produtos") #define o titulo do grafico
# plt.xlabel("Produtos") #define o label do eixo x
# plt.ylabel("Preços") #define o label do eixo y  

# #Grafico2
# plt.figure(figsize=(6, 6)) #define o tamanho da figura
# plt.bar(df["produto"], df["quantidade"], width=0.5, color='#a5ba00') #define o tipo de grafico e os dados que serao utilizados
# plt.title("Gráfico de Quantidades dos Produtos") #define o titulo do grafico
# plt.xlabel("Produtos") #define o label do eixo x
# plt.ylabel("Quantidades") #define o label do eixo y

#Grafico3
plt.figure(figsize=(10, 6)) #define o tamanho da figura  
plt.plot(df["produto"], df["preço"], marker='o', color='#a5ba00') #define o tipo de grafico e os dados que serao utilizados
plt.title("Gráfico de Preços dos Produtos") #define o titulo do grafico 


plt.show() #exibe o grafico


