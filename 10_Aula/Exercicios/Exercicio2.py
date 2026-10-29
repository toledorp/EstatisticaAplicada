# Cálculo do Valor Esperado de Frequência:
# Um dado justo de 6 faces é lançado N = 600 vezes de forma independente.
# Sabendo que a probabilidade teórica de cada face é P(X = x) = 1/6:

# 1. Qual é a frequência esperada de ocorrências para a Face 1?
frequencia_esperada_1 = 600 * (1/6)
print(f"Frequência esperada para a Face 1: {frequencia_esperada_1}")

# 2. Qual é a frequência esperada para a Face 2, 3, 4, 5 e 6?
frequencia_esperada_2 = 600 * (1/6)
frequencia_esperada_3 = 600 * (1/6)
frequencia_esperada_4 = 600 * (1/6)
frequencia_esperada_5 = 600 * (1/6)
frequencia_esperada_6 = 600 * (1/6)

print(f"Frequência esperada para a Face 2: {frequencia_esperada_2}")
print(f"Frequência esperada para a Face 3: {frequencia_esperada_3}")
print(f"Frequência esperada para a Face 4: {frequencia_esperada_4}")
print(f"Frequência esperada para a Face 5: {frequencia_esperada_5}")
print(f"Frequência esperada para a Face 6: {frequencia_esperada_6}")

# 3. Qual é a soma de todas as frequências esperadas?
soma_frequencias_esperadas = (frequencia_esperada_1 + frequencia_esperada_2 + frequencia_esperada_3 +
                              frequencia_esperada_4 + frequencia_esperada_5 + frequencia_esperada_6)    
print(f"Soma de todas as frequências esperadas: {soma_frequencias_esperadas}")
