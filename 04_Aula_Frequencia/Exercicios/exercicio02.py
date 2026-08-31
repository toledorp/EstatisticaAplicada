import pandas as pd
import matplotlib.pyplot as plt

linguagens = [
    "PHP", "PYTHON", "COBOL", "ASSEMBLER", "JAVA",
    "C##", "JAVASCRIPT", "PYTHON", "COBOL", "JAVA",
    "C##", "JAVASCRIPT", "PYTHON", "PHP", "JAVA",
    "PHP", "PYTHON", "COBOL", "ASSEMBLER", "JAVA",
    "C##", "JAVASCRIPT", "PYTHON", "COBOL", "JAVA",
    "C##", "JAVASCRIPT", "PYTHON", "PHP", "JAVA",
]

serie = pd.Series(linguagens)

#Calcule a Frequência
fr_abs = serie.value_counts()
print("Frequencioa Absoluta")
print(fr_abs)

#Calcule a porcentagem
fr_rel = serie.value_counts(normalize=True)
print("Frequencia relativa")
print(fr_rel)

#Identifique o sistema mais frequente
print(fr_abs.idxmax(), fr_abs.max())

#Crie um gráfico de barra
fr_abs.plot(kind="bar")

plt.title("Linguagem de programação")
plt.xlabel("linguagem")
plt.ylabel("Quantidade")
plt.show()

#Crie um gráfico de pizza
fr_abs.plot(
    kind="pie",
    autopct = "%1.1f%%"
)

plt.title("Linguagem de programação")
plt.show()