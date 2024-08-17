def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 15 - Construindo Tabuada')

num = int(input('Digite um número para construir a tabuada: '))

print('*' *35)
print('A tabuada para o número informado é: ')

for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')
