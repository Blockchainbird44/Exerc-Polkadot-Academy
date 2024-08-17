def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 14 - Identificando um Palíndromo')

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
invertido = ''


for letra in range (len(junto) -1, -1, -1):
    invertido += junto[letra]

print('*' *35)
print(f'Comparando as strings temos: {junto} e {invertido}.')

if invertido == junto:
    print('Esta frase é um palíndromo!')
else:
    print('A frase digitada não forma um palíndromo.')
    