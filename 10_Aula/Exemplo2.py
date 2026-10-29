# Simulando 1000 lançamentos de um dado justo de 6 faces usando NumPy
import numpy as np

# configura semente para reprodutibilidade
np.random.seed(42)

# Simula 1000 lançamentos do dado
lancamentos = np.random.randint(1, 7, size=1000)

# exibe os primeiros 20 lançamentos 
print("Primeiros 20 lançamentos do dado:", lancamentos[:20])
