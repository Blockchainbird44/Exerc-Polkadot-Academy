def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 13 - Calculando o IMC')

P = float(input('Informe seu peso em Kg: '))
H = float(input('Informe sua altura: '))

IMC = P / (H**2)

print('*' *35)
print(f'De acordo com os parâmetros informados, seu IMC é {IMC:.2f}.')

if IMC <= 18.5:
    print('Atenção, você está abaixo da faixa de peso normal!')
elif IMC >= 18.5 and IMC <= 24.9:
    print('Seu peso está dentro da faixa. Parabéns!')
elif IMC >= 25 and IMC <= 29.9:
    print('Você está na faixa de sobrepeso, cuide-se!')
elif IMC >= 30 and IMC <= 34.9:
    print('Cuidado, você está na faixa I de OBESIDADE. Procure orientação médica.')
elif IMC >= 35 and IMC <= 39.9:
    print('Atenção, seu IMC está classificado como OBESIDADE faixa II! Procure ajuda médica.')
else:
    print('Seu nível de OBESIDADE está muito acima do limite. Procure ajuda médica imediatamente!')