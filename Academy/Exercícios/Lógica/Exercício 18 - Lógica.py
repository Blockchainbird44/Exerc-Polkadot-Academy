def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 18 - Sequência de Fibonacci')

seq = int(input('Informe quantos termos quer mostrar nesta sequência: '))
t1 = 0
t2 = 1
cont = 3

print('*' *35)
print(f'Esta é a sequência resultante: {t1} -> {t2} ->', end = '')
while cont <= seq:
    t3 = t1 + t2
    print(f' {t3} ->', end = '')
    t1 = t2
    t2 = t3
    cont += 1

print('Fim da sequência.')
