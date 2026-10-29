# Exercício 6 (API)
# Crie uma simulação em Python para 10.000 requisições de uma API:
# 1. Cada requisição tem 95% de chance de Sucesso e 5% de Erro.
# 2. Utilize `np.random.choice()` para simular.
# 3. Calcule o total e a porcentagem de erros obtidos na simulação.

import numpy as np

requicoes = np.random.choice( ["Sucesso", "Erro"] , size=10000, p=[0.95, 0.05])

total = len(requicoes)
total_erros = (requicoes == "Erro").sum()
porcentagem_erro = (total_erros / total ) * 100

print("Total de requições", total)
print("Total de erros", total_erros)
print("Porcentagem de erros", porcentagem_erro, "%")