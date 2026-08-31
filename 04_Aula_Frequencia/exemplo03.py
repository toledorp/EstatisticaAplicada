## Graficos

import pandas as pd
import matplotlib.pyplot as plt

notas = [5, 6, 7, 8, 9, 10]
frequencias = [2, 3, 5, 6, 3, 2]

plt.bar(notas, frequencias)

plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.title("Distribuição das Notas")

plt.show()

## sem dados filtados


## Graficos

import pandas as pd
import matplotlib.pyplot as plt

notas = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 7, 8, 9, 10, 8, 7, 6, 8, 9, 8]

plt.bar(notas, frequencias)

plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.title("Distribuição das Notas")

plt.show()