def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 12 - Convertendo temperaturas')

TC = float(input('Informe a temperatura em °C neste momento: '))

F = (TC * 1.80) + 32
K = TC + 273.15

print('*' * 35)
print(f'Convertendo a temperatura informada em Fahrenheit, temos {F}°F.')
print(f'Convertendo a temperatura informada em Kelvin, temos {K}°K.')