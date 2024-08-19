def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 29 - Média Ponderada')

n = int(input('Informe quantas notas serão lançadas: '))

num = 0
den = 0

for i in range(n):
    nota = float(input('Insira a nota: '))
    peso = int(input('Informe o peso para a nota acima (2, 3 ou 5): '))

    num = num + (nota*peso)
    den = den + peso
    media_pond = num/den


print('*' * 50)
print(f'A média ponderada para o aluno é {media_pond:.2f}.')

if media_pond <=4:
    print('O aluno está reprovado!')
elif media_pond >4 and media_pond <=7:
    print('O aluno está de exame final.')
else:
    print('O aluno foi aprovado!')