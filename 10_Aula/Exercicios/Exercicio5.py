# Modelagem Binomial de Confiabilidade de Sistema:
# Um sistema Web apresenta falha/erro em 5% das requisições (p = 0,05).
# Consideramos um lote de n = 100 requisições e definimos X = número de erros.

from scipy.stats import binom

# 1. Qual a distribuição de probabilidade adequada para modelar X?
#Resp.: Distribuição binomial. A distribuição binomial é adequada para modelar X, pois temos um número fixo de tentativas (n = 100) e uma probabilidade constante de sucesso (p = 0,05).

# A distribuição binomial é adequada para modelar X, pois temos um número fixo de tentativas (n = 100) e uma probabilidade constante de sucesso (p = 0,05).
# 2. Identifique os valores de n e p.
n = 100
p = 0.05

# 3. Qual a probabilidade de ocorrerem EXATAMENTE 3 erros em 100 requisições?
k = 3
prob_exatamente_3 = binom.pmf(k, n, p)
print(f"Probabilidade de EXATAMENTE {k} erros em {n} requisições é de : {prob_exatamente_3:.4f} ({prob_exatamente_3*100:.2f}%)")

# 4. Qual a probabilidade de NENHUM erro ocorrer em 100 requisições (P(X = 0))?
k = 0
prob_nenhum_erro = binom.pmf(k, n, p)   
print(f"Probabilidade de NENHUM erro em {n} requisições é de : {prob_nenhum_erro:.4f} ({prob_nenhum_erro*100:.2f}%)")