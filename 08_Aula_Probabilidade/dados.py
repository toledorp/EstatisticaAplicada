import numpy as np

#Gerar 100.000 lançamentos para cada dado independente
dado1 = np.random.randint(1, 7, 1000)
dado2 = np.random.randint(1, 7, 1000)

#Verificar a probabilidade de ambos sairem 6
resul_duplo_6 = (dado1 == 6) & (dado2 == 6)

prob_simulaçao = resul_duplo_6.mean()
prob_teorica = 1/36

print(resul_duplo_6[:100])

print(
    f"Probabilidade do Experimento: {prob_simulaçao:.4f} ({prob_simulaçao*100:.2f}%)"
)

print(
    f"Probabilidade teorica: {prob_teorica:.4f} ({prob_teorica*100:.2f}%)"
)