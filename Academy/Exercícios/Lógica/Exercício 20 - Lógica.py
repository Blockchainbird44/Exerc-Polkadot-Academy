def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 20 - Par ou impar')

def parimpar():

    num = int(input('Digite um número para verificação: '))

    if num % 2 == 0:
        print('*' *35)
        print(f" -> O número {num} é par!")
    else:
        print('*' *35)
        print(f" -> O número {num} é ímpar!")
    

parimpar()