import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Times": ["Palmeiras", "Flamengo", "Corinthians", "Sao Paulo", "Santos"],
    "Pontos": [48, 46, 41, 38, 35]
}

df = pd.DataFrame(dados)

# Exiba a tabela
print("Exibir a tabela")
print(df)
print(df.to_string())

#Gere um grafico de barras
plt.bar(df["Times"], df["Pontos"])
plt.title("Campeonato Brasileirao")
plt.xlabel("Times")
plt.ylabel("Pontos")

plt.show()