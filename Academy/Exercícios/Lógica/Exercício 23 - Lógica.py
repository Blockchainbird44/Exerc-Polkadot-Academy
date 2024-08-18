def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 23 - Soma pares entre 1 e 100')

print('Qual a soma de todos os números pares entre 1 e 100?')

soma = 0

for i in range(1,100,2):
    soma += i

print('*' *60)
print(f'-> A soma de todos os números pares entre 1 e 100 é: {soma}.')
