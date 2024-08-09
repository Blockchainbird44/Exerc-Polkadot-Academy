def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *40)
    print(tit)
    print("-" *40)


cab_logica('Atividade 9 - Contando a letra')

def conte_letra (frase, letra):
    return sum(1 for char in frase.lower() if char==letra)


frase = input("Digite uma frase para proceder a contagem: \n")
letra = input("Informe qual letra deseja destacar na frase: ")
cont = conte_letra(frase, letra)
print("-" *40)
print(f'A letra "{letra}" aparece {cont} vezes nesta frase.')

