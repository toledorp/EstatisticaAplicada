import numpy as np

resultado_10000 = np.random.randint(1, 7, size=100)

quantidade_cinco = np.sum(resultado_10000 == 5)

probabilidade = quantidade_cinco / len(resultado_10000)

print(f"Quantidade de 5s obtidos: {quantidade_cinco}")
print(f"Probabilidade de 5s obtidos: {probabilidade}")
print(f"Probabilidade real teorica 1/6: {1/6:.4f}")