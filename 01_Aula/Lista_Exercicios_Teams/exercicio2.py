import pandas as pd


estoque = {
    "produto": ["Mouse", "Teclado", "Monitor", "Webcam", "Headset"],
    "preco": [85, 150, 980, 220, 320],
    "quant": [12, 8, 4, 10, 6]
}

df = pd.DataFrame(estoque)

# Quantos produtos existem?
print("Quantidade de itens:")
print(len(df)) #1ª maneira
print(df.shape) #2ª maneira

# Qual possui maior preço?
print("Qual o maior item.")
print(max(df.preco))
# Qual possui menor preço?
print ("Qual o menor preço")
print(min(df.preco))
# Qual a soma das quantidades?
print("Qual a quantidade total do estoque:")
print(sum(df.quant))