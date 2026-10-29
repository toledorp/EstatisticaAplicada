from scipy.stats import binom

# Parâmetros: k = 4 sucessos, n = 10 tentativas, p = 0.3 probabilidade

probabilidade = binom.pmf(k=4, n=10, p=0.3)
print(f"Probabilidade exata P(X = 4): {probabilidade:.4f}")
print(f"Em porcentagem: {probabilidade * 100:.2f}%")