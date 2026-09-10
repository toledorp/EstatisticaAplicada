import pandas as pd

# cpu = [45, 48, 46, 47, 49, 50, 46, 47, 48, 95]
cpu = [45, 48, 46, 47, 49, 50, 46, 47, 48]

serie = pd.Series(cpu)
media = serie.mean()
amp = serie.max() - serie.min()
mediana = serie.median()
desv = serie.std(ddof=0)

print(f"Media: {media}, Mediana: {mediana}, Amplitude: {amp}")
print(f"Desvio padrao: {desv}")