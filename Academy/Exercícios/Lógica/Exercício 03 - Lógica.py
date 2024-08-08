print("     Atividades - Lógica - Polkadot Academy     ")
print("------------------------------------------------")
print("     Atividade 3 - Operações Matemáricas        ")

print("Vamos realizar algumas contas?")

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

soma = num1 + num2
subtracao = num1-num2
prod = num1 * num2
div = num1 / num2
restdiv = num1 % num2

print("De acordo com os números informados, temos: ")
print("____________________________________________")

print('A soma entre {} e {} é igual a {}.'.format(num1, num2, soma))
print('A subtração entre {} e {} é igual a {}.'.format(num1, num2, subtracao))
print('O produto entre {} e {} é igual a {}.'.format(num1, num2, prod))
print('O resultado da fivisão entre {} e {} é igual a {}.'.format(num1, num2, div))
print('O resto da divisão entre {} e {} é igual a {}.'.format(num1, num2, restdiv))

