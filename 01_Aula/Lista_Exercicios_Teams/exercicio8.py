import pandas as pd
import matplotlib.pyplot as plt


# Criando base de dados de Pokémon
dados = {
    "Nome": ["Pikachu", "Charizard", "Blastoise", "Venusaur", "Dragonite", 
             "Alakazam", "Machamp", "Golem", "Arcanine", "Lapras"],
    "Tipo": ["Eletrico", "Fogo/Voador", "Agua", "Grama/Veneno", "Dragao/Voador",
             "Psiquico", "Lutador", "Rocha/Terra", "Fogo", "Agua/Gelo"],
    "Nivel": [25, 36, 34, 32, 55, 26, 36, 30, 32, 30]
}

df = pd.DataFrame(dados)

# Exibindo a tabela
print("Base de Dados - Pokemon")
# Exiba a tabela
print(df)
# Utilize head().
print(df.head())
# Utilize describe().
print(df.describe())
# Utilize info().
print(df.info())

# Gere um gráfico de barras.
plt.bar(df["Nome"], df["Nivel"])
plt.title("Nivel poder Pokemons")
plt.xlabel("Nome")
plt.ylabel("Nivel")

plt.show()

# Informações adicionais (opcional)
print("\n--- Informacoes ---")
print(f"Total de Pokemon: {len(df)}")
print(f"Nivel Medio: {df['Nivel'].mean():.2f}")
print(f"Pokemon de maior nivel: {df.loc[df['Nivel'].idxmax(), 'Nome']} (Nivel {df['Nivel'].max()})")


