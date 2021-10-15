#jogo de adivinhação
from  random import randint
computador = randint(1, 10)
jogador = 0
jogadas = 1
while jogador != computador:
    jogador = int(input('tente adivinhar o numero pensado pelo computador (de 0 a 10) '))
    if jogador != computador:
        jogadas += 1
if jogadas == 1:
    print('parabens você acertou de primeira')
print(f'o numero pensado pelo computador foi {computador} e você precisou de exatas {jogadas} jogadas para acertar ')