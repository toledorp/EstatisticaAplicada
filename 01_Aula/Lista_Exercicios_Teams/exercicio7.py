import pandas as pd
c

# Define nomes para os alunos
nomes = ["Ana Silva", "Bruno Costa", "Carlos Santos", "Diana Oliveira", "Eduardo Lima",
         "Fernanda Gomes", "Gabriel Pereira", "Helena Martins", "Igor Ferreira", "Julia Rocha",
         "Kevin Alves", "Laura Souza", "Matheus Neves", "Natalia Cardoso", "Oscar Barbosa",
         "Patricia Ribeiro", "Qualquer Diniz", "Rafael Mendes", "Sandra Vasconcelos", "Tiago Correia"
        ]

# Gera dados aleatórios
dados = {
    "Nome": nomes,
    "Idade": np.random.randint(18, 30, 20),  # Idade entre 18 e 29 anos
    "Nota": np.round(np.random.uniform(1, 10, 20), 2)  # Nota entre 0 e 10
}

df = pd.DataFrame(dados)

# Exiba o DataFrame.
print("Exibindo o DataFrame")
print(df)

# Utilize head().
print("Utilizando head")
print(df.head())

# Utilize describe().
print("Utilizando describe")
print(df.describe())

# Utilize info().
print("Utilizando info")
print(df.info())