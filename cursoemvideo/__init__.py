def metade(numero, formatacao=False):
    if formatacao == True:
        meio = numero / 2
        return f'R${meio:.2f}'
    else:
        meio = numero / 2
        return meio


def dobro(numero, formatacao=False):
    if formatacao == True:
        dobr = numero * 2
        return f'R${dobr:.2f}'
    else:
        dobr = numero * 2
        return (dobr)


def aumentando(numero, porcentagem = 0, formatacao=False):
    if formatacao == True:
        dez = (numero * porcentagem / 100) + numero
        return f'R${dez:.2f}'
    else:
        dez = (numero * porcentagem / 100) + numero
        return dez


def reduzindo(numero, porcentagem = 0, formatacao=False):
    if formatacao == True:
        reduçao = numero - (numero * porcentagem / 100)
        return f'R${reduçao:.2f}'
    else:
        reduçao =  numero - (numero * porcentagem / 100)
        return reduçao

def moeda(numero):
    return f'R${numero:.2f}'

def resumo(numero, aumento=0, reducao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.rjust(22))
    print('-' * 30)
    print(f'Preço analisado:      R${numero:<5}')
    print(f'Dobro do preço:       R${numero*2:<5}')
    print(f'metade do preço:      R${numero/2:<5}')
    print(f'{aumento} de aumento:        R${numero * aumento / 100 + numero:<12}')
    print(f'{reducao} de reducao:         R${numero - numero * reducao / 100:<13}')
    print('-' * 30)