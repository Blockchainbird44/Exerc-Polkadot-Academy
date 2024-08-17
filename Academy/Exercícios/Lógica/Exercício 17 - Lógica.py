def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 17 - Calculando média aluno')

quant_nota = 0
soma_nota = 0

while True:
    lnota= float(input('Insira uma nota (ou digite -1 para encerrar a inserção): '))
    if lnota == -1:
        break
    soma_nota += lnota
    quant_nota += 1

if quant_nota == 0:
    print('Nenhuma nota inserida. Insira uma nota válida.')
else:
    media_nota = soma_nota/quant_nota

print('*' *35)

print(f'Foram lançadas {quant_nota} para este aluno.')
print(f'A média das notas lançadas é {media_nota:.2f}.')

if media_nota <= 4:
    print(f'Com média {media_nota:.2f}, está reprovado na disciplina!')
elif media_nota >= 4.1 and media_nota<= 7:
    print(f'Com média {media_nota:.2f}, está de exame final na disciplina.')
else:
    print(f'Com média {media_nota:.2f} está aprovado, parabéns!')

