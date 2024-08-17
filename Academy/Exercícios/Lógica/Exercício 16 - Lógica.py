def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 16 - Contando vogais')


def cont_vogais():
    F = str(input('Insira a frase para iniciar a contagem: '))
    V = 'aáàãeéẽiíoóõuúAÁEÉIÍOÓUÚ'
    c = 0

    for vog in F:
        if vog in V:
            c += 1

    print('*' *35)
    print(f'>> A frase inserida acima possui {c} vogais.')

cont_vogais()
  



