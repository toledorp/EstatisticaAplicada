import numpy as np

#Gerar 100.000 lançamentos para cada dado independente
dado1 = np.random.randint(1, 7, 100000)
dado2 = np.random.randint(1, 7, 100000)

#Verificar a probabilidade de ambos sairem 6
resul_duplo_1 = (dado1 == 1) & (dado2 == 1)
resul_duplo_2 = (dado1 == 2) & (dado2 == 2)
resul_duplo_3 = (dado1 == 3) & (dado2 == 3)
resul_duplo_4 = (dado1 == 4) & (dado2 == 4)
resul_duplo_5 = (dado1 == 5) & (dado2 == 5)
resul_duplo_6 = (dado1 == 6) & (dado2 == 6)

result_duplo_igual = (dado1 == dado2)
soma_result_duplo = result_duplo_igual.mean()


prob_simulaçao = resul_duplo_1.mean()
prob_simulaçao = resul_duplo_2.mean()
prob_simulaçao = resul_duplo_3.mean()
prob_simulaçao = resul_duplo_4.mean()
prob_simulaçao = resul_duplo_5.mean()
prob_simulaçao = resul_duplo_6.mean()

prob_teorica = 1/36

print(resul_duplo_6[:100])

print(
    f"Probabilidade do Experimento: {prob_simulaçao:.4f} ({prob_simulaçao*100:.2f}%)"
)

print(
    f"Probabilidade teorica: {prob_teorica:.4f} ({prob_teorica*100:.2f}%)"
)