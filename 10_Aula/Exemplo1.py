# Modelando a distribuição de probabilidade de um dado justo de 6 faces usando NumPy

import numpy as np

#Valores possiveis do dado (1 a 6)
resultados = np.arange(1, 7)

#Probabilidade uniforme de 1/6 para cada face
probabilidade = np.ones(6) / 6

print("Resultado do lançamento do dado:", resultados)
print("Probabilidade de cada face:", probabilidade)


