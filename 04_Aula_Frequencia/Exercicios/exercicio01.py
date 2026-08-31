import pandas as pd
import matplotlib.pyplot as plt

notas = [
    7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10
]

#Criar uma serie
serie = pd.Series(notas)

#Calcular uma frequencia absoluta
fabs = serie.value_counts()

##Calcular a frequencia relativa
frel = serie.value_counts(normalize=True)

##Calcular a frequencia acumulada
facum = fabs.cumsum

## Criando uma tabela
tabela = pd.DataFrame({
    "Frequencia_Absoluta": fabs,
    "Frequencia_Relativa": frel,
    "Frequencia_Acumulada": facum 
})

print(tabela)


# #Criar um grafico de barras
fabs.plot(kind="bar")

plt.title("Frequencvia das Notas")
plt.xlabel("Notas")
plt.ylabel("Frequencia")

plt.show()

# #Criar grafico de pizza
fabs.plot(
    kind="pie",
    autopct = "%1.1f%%"
)

plt.title("Frequencia das notas")
plt.show()

