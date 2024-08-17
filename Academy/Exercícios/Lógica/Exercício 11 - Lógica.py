def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 11 - Calculando Fatorial')

num = (int(input('Digite um número inteiro para o cálculo do fatorial: ')))
cont = num
fat = 1
print('*' *30)
print(f'Calculando {cont}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont-=1

print(f'{fat}')


