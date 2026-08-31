import pandas as pd

lista = [12, 25, 18, 40, 32, 11, 9, 28, 37, 15]
df = pd.DataFrame({"Valores": lista})

# Calcule:
#  Quantidade de elementos.
print("Quantidade de elementos")
print(len(lista))

#  Soma.
print("Soma do valores")
print(sum(lista))

#  Média (ex: print(df["Nota"].mean())).
print("Media dos valores")
print(df["Valores"].mean())

#  Maior valor.
print("Maior valor")
print(max(lista))

#  Menor valor.
print("Menor valor")
print(min(lista))

# Desafio:
#  Ordene a lista em ordem crescente.
print("Lista em ordem crescente")
print(sorted(lista))

#  Ordene a lista em ordem decrescente.
print("Lista em ordem decrescente")
print(sorted(lista, reverse=True))