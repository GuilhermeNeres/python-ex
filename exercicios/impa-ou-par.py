#jogo de impa oupar

from random import randint

jogadas = 0
computador = randint(1, 100)
jogador = 0
soma = 0
decisao = ''
while True:
    jogador = int(input('digite um numero '))
    decisao = input('I/P ').upper()
    soma = (jogador + computador) % 2
    if soma == 1 and decisao == 'I':
        print(f'Você escolheu o numero {jogador} e a maquina o {computador}, deu impar e voce escolheu impar, portanto voce venceu!')
    elif soma == 0 and decisao == 'P':
        print(f'Vôce escolheu o numero {jogador} e a maquina o {computador}, deu par e voce escolheu par, portanto voce venceu!')
    elif soma == 1 and decisao == 'P':
        print(f'Você escolheu o numero {jogador} e a maquina o {computador}, deu impar e voce escolheu par, portanto você perdeu!')
        break
    elif soma == 0 and decisao == 'I':
        print(f'Você escolheu o numero {jogador} e a maquina o {computador}, deu par e voce escolheu impar, portanto voce perdeu!')
        break
    jogadas += 1
if jogadas == 0:
    print('você nao conseguiu ganhar nenhuma vez, mais sorte na proxima :)')
else:
    print(f'Você conseguiu ganhar {jogadas} vezes antes de perder, parabens!')
