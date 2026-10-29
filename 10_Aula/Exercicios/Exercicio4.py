# Cálculo Binomial de Engajamento:
# Uma aplicação envia uma notificação push para n = 20 usuários.
# A probabilidade histórica de um usuário clicar na notificação é p = 0,40 (40%).
# Utilizando scipy.stats.binom, responda:
# 1. Qual a probabilidade de EXATAMENTE k = 8 usuários clicarem na notificação?
# 2. Apresente o resultado em porcentagem formatada.


from scipy.stats import binom

n = 20  # número de usuários
p = 0.40  # probabilidade de sucesso
k = 8  # número de usuários que clicam

# 1. Probabilidade de EXATAMENTE k = 8 usuários clicarem
prob_exatamente_k = binom.pmf(k, n, p)

# 2. Apresente o resultado em porcentagem formatada
print(f"Probabilidade de EXATAMENTE {k} usuários clicarem é de : {prob_exatamente_k:.4f} ({prob_exatamente_k*100:.2f}%)")