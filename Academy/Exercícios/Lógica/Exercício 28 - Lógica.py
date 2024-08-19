def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 28 - Contagem de Palavras')

frase = str(input('Insira a frase para iniciar a contagem de palavras: '))

palavras = frase.split()

cont_palavras = len(palavras)

print('*' *50)
print(f'-> A frase digitada possui {cont_palavras} palavras.')