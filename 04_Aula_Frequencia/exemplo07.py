

import pandas as pd
import matplotlib.pyplot as plt

tempos = [
    120, 130, 115, 140, 150,
    180, 175, 190, 210, 220,
    250, 280, 300, 320, 350
]

plt.hist(tempos, bins=5)

plt.xlabel("Tempo de resposta (ms)")
plt.ylabel("Frequência")
plt.title("Tempo de Resposta do Sistema")

plt.show()