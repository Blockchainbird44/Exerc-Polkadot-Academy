def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 24 - Calculadora')

def calcular(op1, op2, operador):
    if operador == '+':
        return op1 + op2
    elif operador == '-':
        return op1 - op2
    elif operador == '*':
        return op1 * op2
    elif operador == '/':
        if op2 != 0:
            return op1 / op2
        else:
            return 'Erro: Não é possível dividir por 0(zero).'
    
op1 = int(input('Insira o primeiro operando: '))
op2 = int(input('Insira o segundo operando: '))
operador = str(input('Agora escolha o operador (+ , - , * ou /): '))

resultado = calcular(op1, op2, operador)

print('*' *50)
print(f'O resultado da operação é: {op1} {operador} {op2} = {resultado:.0f}')

