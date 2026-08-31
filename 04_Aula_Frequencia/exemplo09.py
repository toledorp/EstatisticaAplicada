## Grafico Outlies

import pandas as pd
import matplotlib.pyplot as plt

tempos = [
    120, 130, 115, 140, 150,
    180, 175, 190, 210, 220,
    250, 280, 300, 320, 350
]

plt.boxplot(tempos)

plt.ylabel("Tempo (ms)")
plt.title("Distribuição do Tempo de Resposta")

plt.show()