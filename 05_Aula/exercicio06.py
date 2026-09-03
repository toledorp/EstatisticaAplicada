import pandas as pd

GA = [10, 10, 10, 10, 10]
GB = [2, 4, 6, 10, 14, 18]

# 1. Calcule a média e a mediana para os dois grupos e compare os resultados obtidos.
media_A = pd.Series(GA).mean()
mediana_A = pd.Series(GA).median()
media_B = pd.Series(GB).mean()
mediana_B = pd.Series(GB).median()

print("Grupo A:")
print("Média:", media_A)
print("Mediana:", mediana_A)
print("\nGrupo B:")
print("Média:", media_B)
print("Mediana:", mediana_B)

# 2. Pergunta crítica: As medidas de tendência central são suficientes para afirmar que ambos os
#    grupos possuem exatamente o mesmo comportamento?


# 3. Justifique o porquê de os grupos serem estruturalmente diferentes, apesar de possuírem médias e
#    medianas idênticas.