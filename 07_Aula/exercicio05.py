# Exercício 5 (Dado)
# Escreva um programa em Python usando NumPy e Pandas para:
# 1. Simular 10.000 lançamentos de um dado.
# 2. Calcular a frequência relativa de CADA uma das 6 faces (1 a 6).
# 3. Comparar os resultados obtidos com a probabilidade teórica de 1/6 (16.67%).

import numpy as np
import pandas as pd

lancamentos = np.random.randint(1, 7, size=10000)

serie = pd.Series(lancamentos)

frequencia = serie.value_counts().sort_index()
frequencia_relativa = frequencia / len(lancamentos)

probabilidade_teorica = 1/6

tabela = pd.DataFrame({
    "Frequencia": frequencia,
    "Frequencia Relativa": frequencia_relativa * 100,
    "Probabilidade Teórica": probabilidade_teorica * 100
})

print(tabela)