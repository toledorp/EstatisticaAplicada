import pandas as pd

alunos = pd.DataFrame({
    "Nome":[
        "Ana", "Bruno", "Calor", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena","Igor", "Juliana", "Lucas", "Marina"
    ],
    "Notas":[
        8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10 
    ]
})

# tamanho da população
print(alunos.shape[0])
print(len(alunos))

# Calculo média da população

#Retire uma amostra de 5 alunos
amostra = alunos.sample(n=5, random_state=42)

#Calcule a média da amostra
media_amostra = amostra["Notas"].mean()
print(media_amostra)

# Compare as duas médias
print(media_populacao - media_amostra)

# com 8 alunos
amostra = alunos.sample(n=5, random_state=42)
