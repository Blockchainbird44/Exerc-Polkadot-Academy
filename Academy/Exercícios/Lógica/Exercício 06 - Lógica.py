print("     Atividades - Lógica - Polkadot Academy     ")
print("------------------------------------------------")
print("   Atividade 6 - Soma de valores informados     ")

n = int(input("Digite abaixo os valores para a soma ou digite 0 para encerrá-la: \n"))

i = 0
soma = 0

while (i < n):
    s = int(input())
    soma = soma + s
    i = i+1
    if (s == 0):
        print("A soma dos valores digitados é {}".format(soma))
