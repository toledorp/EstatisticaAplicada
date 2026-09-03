import pandas as pd
import matplotlib.pyplot as plt

linguagem = pd.Series(["Python", "Java", "Python", "JavaScript", "Python",  "C#", "Java", "Python", "C#", "Python"])

# 1. Converta a lista de linguagens em uma Series do Pandas.
serie = pd.Series(linguagem)

# 2. Calcule a frequência absoluta de cada uma e descubra qual linguagem é a Moda do conjunto.
frequencia = serie.value_counts()
print("Frequência absoluta de cada linguagem:\n")
print(frequencia)

# 3. Calcule a frequência relativa em porcentagem para cada categoria registrada.
freq_rel = serie.value_counts(normalize=True) * 100
print("Frequência relativa em porcentagem:\n")
print(freq_rel)

# calculo da moda
moda = frequencia.idxmax()
print("A linguagem mais popular (Moda) é:", moda)   


# 4. Crie um Gráfico de Barras com Matplotlib mostrando a preferência das linguagens.
plt.bar(frequencia.index, frequencia.values)
plt.xlabel("Linguagem")
plt.ylabel("Frequência Absoluta")
plt.title("Preferência das Linguagens de Programação")
plt.show()