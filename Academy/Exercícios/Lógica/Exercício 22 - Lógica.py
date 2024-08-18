def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 22 - Advinhe se puder!')

from random import randint

computador = randint( 0, 100)

print('Olá, jovem Padawan, bom em advinhar quero saber se você é!')
print('Um número aleatório entre 0 e 100 escolhi, e qual foi quero que advinhe.')
print('Então, aceitar o desafio vai você ou se esconder num canto da galáxia irá?')

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Seu palpite qual será?: '))
    palpite += 1
    
    if jogador == palpite:
        acertou = True
    else:
        if jogador < computador:
            print('Hum, acertar não conseguiu. O número maior é... Tentar de novo deve você!')
        elif jogador > computador:
            print('Hum, acertar não conseguiu. O número menor é... Tentar de novo deve você!')
        else:
            if palpite <= 33:
                print('*' *60)
                print(f'De parabéns está você. Em menos de {palpite} tentativas acertou!')
            elif palpite > 34 and palpite <= 66:
                print('*' *60)
                print(f'Treinar mais deve você! O desafio acertou em {palpite} tentativas.')
            else:
                print('*' *60)
                print(f'Muito treinamento ainda precisa, de {palpite} tentativas precisou. Hum...Hum...muito mal!')
            break

