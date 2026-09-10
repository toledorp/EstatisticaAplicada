import pandas as pd

gA = [100, 100, 100, 100, 100]
gB = [80, 90, 100, 110, 120]

serieA = pd.Series(gA)
serieB = pd.Series(gB)

# 1. A média aritmética e a amplitude
print("Grupo A")
print(f"Media: {serieA.mean()}, Amplitude: {serieA.max() - serieA.min()}")
print(f"Variancia Amostral : {serieA.var()}, Variancia Populacional {serieA.var(ddof=0)}")
print(f"Desvio padrao amostral {serieA.std()}, Desvio padroia Populacional: {serieA.std(ddof=0)}")

print("Grupo B")
print(f"Media: {serieB.mean()}, Amplitude: {serieB.max() - serieB.min()}")
print(f"Variancia Amostral : {serieB.var()}, Variancia Populacional {serieB.var(ddof=0)}")
print(f"Desvio padrao amostral {serieB.std()}, Desvio padroia Populacional: {serieB.std(ddof=0)}")
