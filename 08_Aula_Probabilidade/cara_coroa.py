import numpy as np

#Lançar a moda 10000 vezes
resultados = np.random.choice(["Cara", "Coroa"], size=10000)

# Mostra os 30 primeiros
print (
    f"primeiros 30 resultados dos alnçamentos : ${resultados[:30]}"
)


#Contando a quantidade de caras
caras = np.sum(resultados == "Cara")

#Probabilidade de cara na simulação
prob_simulacao = caras / len(resultados)

print(
    f"Total de caras : {caras}"
)

print(
    f"Probabilidade experimental: {prob_simulacao *100:.2f} %"
)

print(
    f"Probabilidade teórica: {(1/2)*100:.2f}%"
)
