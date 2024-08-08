print("     Atividades - Lógica - Polkadot Academy     ")
print("------------------------------------------------")
print("    Atividade 4 - Como está a temperatura?      ")

temp = float(input("Informe a temperatura neste momento: "))

if temp <= 19:
    print("A temperatura está baixa neste momento. Use agasalho!")
elif temp >=19.1 and temp <= 25:
    print("A temperatura está agradável neste momento.")
elif temp >= 25.1 and temp <= 35:
    print("A temperatura está elevada neste momento. Beba água! ")
else:
    print("A temperatura está muito elevada. Cuide-se!")
     
   


