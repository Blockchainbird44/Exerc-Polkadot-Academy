def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 27 - Número Perfeito')

def num_perfeito():
    numero = int(input('Informe um número inteiro: '))

    soma_div = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma_div += i

    if soma_div == numero:
        print('*' *50)
        print(f'{numero} é um número perfeito!')
    else:
        print('*' *50)
        print(f'{numero} não é um número perfeito!')

    print(f'A soma dos divisores do número {numero} é {soma_div}.')


num_perfeito()

