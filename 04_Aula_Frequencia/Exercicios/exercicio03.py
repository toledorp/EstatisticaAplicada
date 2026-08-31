import pandas as pd
import matplotlib.pyplot as plt

sistemas = [
    "Windows", "Linux", "Android", "Windows", "macOS",
    "Windows", "iOS", "Linux", "Windows", "Android",
    "macOS", "Windows", "Linux", "Windows", "Android",
    "Windows", "macOS", "Linux", "iOS", "Windows",
    "Android", "Windows", "Linux", "macOS", "Windows",
    "Android", "Linux", "Windows", "macOS", "Windows",
    "iOS", "Android", "Linux", "Windows", "macOS",
    "Windows", "Android", "Linux", "Windows", "Windows",
    "macOS", "Android", "Windows", "Linux", "iOS",
    "Windows", "Android", "macOS", "Linux", "Windows"
]

serie = pd.Series(sistemas)

# Calcule a frequência absoluta
frequencia_absoluta = serie.value_counts()
print("Frequência absoluta:")
print(frequencia_absoluta)

# Calcule a frequência relativa em porcentagem
frequencia_relativa = serie.value_counts(normalize=True).mul(100)
print("\nFrequência relativa (%):")
print(frequencia_relativa.round(2))

# Identifique o sistema mais frequente
sistema_mais_frequente = frequencia_absoluta.idxmax()
quantidade = frequencia_absoluta.max()
print(f"\nSistema mais frequente: {sistema_mais_frequente} ({quantidade} ocorrências)")

# Crie um gráfico de barras
plt.figure(figsize=(8, 5))
frequencia_absoluta.plot(kind="bar", color="steelblue")
plt.title("Sistemas Operacionais")
plt.xlabel("Sistema")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Crie um gráfico de pizza
plt.figure(figsize=(7, 7))
frequencia_absoluta.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    ylabel=""
)
plt.title("Sistemas Operacionais")
plt.tight_layout()
plt.show()
