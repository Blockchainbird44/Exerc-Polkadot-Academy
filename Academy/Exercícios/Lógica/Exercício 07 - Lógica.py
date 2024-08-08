print("     Atividades - Lógica - Polkadot Academy     ")
print("------------------------------------------------")
print("         Atividade 7 - Lista de Compras         ")

lista = list()
while True:
    item = str(input("Insira um item à lista: "))
    if item not in lista:
        lista.append(item)
        print("> OK, item adicionado!")
    else:
        print("> Este item já foi adicionado anteriormente.")
    add = str(input("Quer adicionar outro item? [S/N] "))
    if add in 'Nn':
        break

print("**" *30)
print(f"Sua lista de compras está completa: {lista}\n")