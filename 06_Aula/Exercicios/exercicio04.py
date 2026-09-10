import pandas as pd

tempos = [110, 115, 120, 112, 118, 121, 117, 113, 119, 300]

serie = pd.Series(tempos)
media = serie.mean()
mediana = serie.median()


print(f"Media {media}, mediana {mediana}")

amp = serie.max() - serie.min()
var = serie.var(ddof=0)
desv = serie.std(ddof=0)
print(f"Amplitude: {amp}, Variancia: {var}, Desvio Padrao: {desv}")