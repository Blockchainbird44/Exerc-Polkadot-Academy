def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 19 - Ordenação de Números')

numeros = []


while True:
    n = int(input('Digite um número ou digite -1 para parar: '))
    if n == -1:
        break
    numeros.append(n)

for i in range(len(numeros)):
    ini = i
    for prox in range(i+1, len(numeros)):
        if numeros[prox] < numeros[ini]:
            ini = prox
        numeros[i], numeros[ini] = numeros[ini], numeros[i]

print('*' *35)
print(f'A lista ordenada terá os seguintes números: {numeros}.')



