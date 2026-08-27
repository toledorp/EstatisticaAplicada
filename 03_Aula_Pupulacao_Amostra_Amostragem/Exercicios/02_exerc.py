import pandas as pd


alunos = pd.DataFrame({
    "Nome":["Ana", "Carlos", "João", "Felipe", "Marcos", "José"],
    "Idade":[20, 25, 63, 10, 58, 25],
    "Notas":[10, 5, 9, 8, 7, 3]
})

#Calcule a media da populaçao
media_populacao = alunos["Idade"].mean()
print(f"Media da população: {media_populacao}")

#selecione aleatoriament 5 alunos
amostra = alunos.sample(n=5, random_state=20)

#Calcule a média da amostra
media_amostra = amostra["Idade"].mean()
print(f"Media amostra : {media_amostra}")

#Selecione aleatoriamente 10 alunos
amostra_10 = alunos.sample(n=6, random_state=20)

#Calcule novamente a média
media_amostra_10 = amostra_10["Idade"].mean()
print(f"Média da amostra com10: {media_amostra_10}")

#Compare os resultados.
