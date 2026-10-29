# Simulação da Distribuição de um Dado (10.000 Lançamentos):
# Escreva um script Python usando NumPy e Pandas para simular 10.000 lançamentos de um dado de 6
# faces e calcule:
import numpy as np
import pandas as pd

np.random.seed(42)  # Para reprodutibilidade dos resultados

# 1. A frequência absoluta observada de cada face;
lancamentos = np.random.randint(1, 7, size=10000)

dados = pd.DataFrame({"face": lancamentos})

frequencia_absoluta = dados['face'].value_counts().sort_index()
frequencia_relativa = dados['face'].value_counts(normalize=True).sort_index()

probabilidade_face_6 = (dados['face'] == 6).mean()
probabilidade_par = (dados['face'] % 2 == 0).mean()

print("Frequência absoluta observada de cada face:")
print(frequencia_absoluta)

# 2. A frequência relativa (proporção) de cada face;
frequencia_relativa = frequencia_absoluta / len(lancamentos)
print("\nFrequência relativa (proporção) de cada face:")
print(frequencia_relativa)

# 3. A probabilidade experimental de obter a Face 6;
probabilidade_face_6 = frequencia_relativa.loc[6]
print(f"\nProbabilidade experimental de obter a Face 6: {probabilidade_face_6}")

# 4. A probabilidade experimental de obter um número PAR (Faces 2, 4, 6).
probabilidade_par = frequencia_relativa.loc[[2, 4, 6]].sum()
print(f"Probabilidade experimental de obter um número PAR: {probabilidade_par}")