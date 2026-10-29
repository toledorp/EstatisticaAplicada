p_spam = 0.10
p_palavra_spam = 0.80
p_palavra_normal = 0.05
p_normal = 1 - p_spam
# Probabilidade Total da Evidência P(Palavra)
p_palavra = (p_palavra_spam * p_spam) + (p_palavra_normal * p_normal)
# Aplicação do Teorema de Bayes
p_spam_dado_palavra = (p_palavra_spam * p_spam) / p_palavra
print("Resultado em Decimal:", p_spam_dado_palavra)