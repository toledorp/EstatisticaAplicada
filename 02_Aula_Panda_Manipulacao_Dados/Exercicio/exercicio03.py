import pandas as pd

dados = {
    "Alunos": ["Ana", "Fernanda", "João", "Carlos", "Ricardo", "Camila", "Angela", "Sergio", "Fabio", "Jose"],
    "Idade": [18, 22, 30, 34, 24, 26, 19, 42, 56, 37],
    "Nota": [6.5, 7, 8.2, 9.1, 6, 4, 8, 7, 7, 5.5]
}

df = pd.DataFrame(dados)

