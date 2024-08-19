def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 26 - Invertendo uma String')

palavra = str(input('Insira uma palavra:'))

inversa = palavra[::-1]

print('*' *50)
print(f'-> A versão invertida da palavra {palavra.upper()} é {inversa.upper()}.')
