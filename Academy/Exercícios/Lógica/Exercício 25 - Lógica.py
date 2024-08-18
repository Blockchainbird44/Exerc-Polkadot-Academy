def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 25 - Soma números intervalo')

def soma_numeros(n):
    soma = 0
    for i in range (1, n + 1):
        soma += i
    return soma
    

n = int(input('Digite um número para realizar a soma no intervalo: '))
resultado = soma_numeros(n)

print('*' *50)
print(f'-> A soma dos primeiros {n} números naturais é: {resultado}.')

