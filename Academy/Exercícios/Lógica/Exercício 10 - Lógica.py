def cab_logica(tit):
    print("Atividades - Lógica - Polkadot Academy")
    print("-" *45)
    print(tit)
    print("-" *45)


cab_logica('Atividade 10 - Encontrando numeros primos')


def encontra_primos(num):
    lista = [True] * (num+1)
    lista[0] = lista[1] = False
    for p in range(2, int(num ** 0.5)+1):
        if lista[p]:
            for i in range(p * p, num+1, p):
                lista[i] = False
    return [p for p in range(2, num+1) if lista[p]]


def primos():

    inicio = int(input("Defina o número de início do intervalo: "))
    fim = int(input("Defina o numero final do intervalo: "))

    primo = encontra_primos(fim)
    print(" -> Números primos no intervalo [{}, {}]: {}".format(inicio, fim, [p for p in primo if inicio <= p <= fim]))

primos()