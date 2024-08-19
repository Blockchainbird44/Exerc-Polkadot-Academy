def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 30 - Maior e Média na Lista')

numeros = []

while True:
    numero = int(input('Insira um número para a lista (ou 0 para sair): '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

if not numeros:
    print('Lista vazia. Por favor insira um número.')
else:
    maior_num = max(numeros)
    print('*' *50)
    print(f'O maior número encontrado na lista é: {maior_num}')

    menor_num = min(numeros)
    print(f'O menor número encontrado na lista é: {menor_num}')

    soma_num = sum(numeros)
    media = soma_num/len(numeros)

    print(f'-> A média dos números envontrados na lista é: {media:.0f}')