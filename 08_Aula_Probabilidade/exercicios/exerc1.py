import numpy as np

# Um dado honesto de 6 faces é lançado uma vez. Determine:

# a) A probabilidade de obter o número 2: P(2)
dado = np.random.randint(1, 7, 1)

resul_prob_2 = (dado == 2)

print(resul_prob_2)



# b) A probabilidade de obter o número 2 OU o número 5: P(2 ∪ 5)
# c) A probabilidade de obter o número 2 E o número 5: P(2 ∩ 5)
# d) A probabilidade de obter um número par: P(Par)