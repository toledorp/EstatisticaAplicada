import pandas as pd
import matplotlib.pyplot as plt

tempos = pd.Series([100, 105, 110, 108, 115, 120, 125, 130, 500, 550])

print("Média dos tempos:", tempos.mean())
print("Mediana dos tempos:", tempos.median())

maior_frequencia = tempos.value_counts().max()

if maior_frequencia > 1:
    print("Moda dos tempos:", tempos.mode().tolist())
else:
    print("Não há moda, pois nenhum tempo se repete.")

print("Menor tempo:", tempos.min())
print("Maior tempo:", tempos.max())

#Criando um gráfico de histograma para visualizar a distribuição dos tempos
plt.hist(tempos)
plt.title('Distribuição dos Tempos')
plt.xlabel('Tempos')    
plt.ylabel('Frequência')
plt.show()

#Criando um gráfico de Boxplot para visualizar a distribuição dos tempos
plt.boxplot(tempos)
plt.title('Distribuição dos Tempos')
plt.ylabel('Tempos (ms)')
plt.show()