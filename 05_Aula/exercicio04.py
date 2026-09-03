import pandas as pd
import numpy as np

tempo = [100, 200, 500]
quantidade = [500, 300, 200]

#utilizaando compreensão de lista e zip()
numerador = sum(
    tempo * quantidade
    for tempo, quantidade in zip(tempo, quantidade)
)
denominador = sum(quantidade)
media_pond = numerador / denominador

#utilizando numpy e a função np.average()
media_pond_numpy = np.average(
    tempo, 
    weights=quantidade
)

print("Media ponderada dos tempos com python simples: ", media_pond)
print("Media ponderada dos tempos com numpy: ", media_pond_numpy)

