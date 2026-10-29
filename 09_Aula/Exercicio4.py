P_Spam = 0.15
P_Nao_Spam = 0.85
P_Palavra_Spam = 0.90
P_palavra_Nao_Spam = 0.04

formula = (P_Palavra_Spam * P_Spam) + (P_palavra_Nao_Spam * P_Nao_Spam)

formula2 = (P_Palavra_Spam * P_Spam) 
formula2 = (P_Palavra_Spam * P_Spam) 

formula3 = (formula2 / formula)

print(formula)
print(formula2)

print(formula3)
