P_Ataque = 0.02
P_Nao_Ataque = 0.98
P_Caso_Ataque = 0.95
P_Alerta_Nao_Ataque = 0.03

Formula_P_Ataque = (P_Caso_Ataque * P_Ataque) + (P_Alerta_Nao_Ataque * P_Nao_Ataque)

Formula2 = (P_Caso_Ataque * P_Ataque) / Formula_P_Ataque

print(Formula2)