def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 21 - Calculando área do círculo')

import math

raio = float(input('Informe o raio (em cm) do círculo para calcular sua área: '))

area = math.pi * raio**2
area_m = area / 100
print('*' *35)
print(f'A área do círculo será {area:.1f} cm², ou , {area_m:.1f} m².')