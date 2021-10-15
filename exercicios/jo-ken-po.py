#um jogo de jokenpo simples

from random import randint
import time

a = randint(1, 3)
jogador = int(input('Digite 1 para pedra\nDigite 2 para papel\nDigite 3 para tesoura\n'))
print('\033[35mJO\033[m')
time.sleep(1)
print('\033[35mKEN\033[m')
time.sleep(1)
print('\033[35mPO\033[m')
if a == 1 and jogador == 1:
    print('A maquina escolheu \033[31mpedra\033[m\nO jogador escolheu \033[31mpedra\033[m\n\033[97mJOGO EMPATADO\033[m')
elif a == 2 and jogador == 1:
    print('A maquina escolheu \033[31mpapel\033[m\nO jogador escolheu \033[31mpedra\033[m\nisso é uma vitoria da maquina')
elif a == 3 and jogador == 1:
    print('a maquina escolheu \033[31mtesoura\033[m\nO jogador escolheu \033[31mpedra\033[m\n isso é uma vitoria para o jogador')
elif a == 1 and jogador == 2:
    print('a maquina escolheu \033[31mpedra\033[m\nO jogador escolheu \033[31mpapel\033[m\nisso é uma vitoria para o jogador')
elif a == 2 and jogador == 2:
    print('a maquina escolheu \033[31mpapel\033[m\nO jogador escolheu \033[31mpapel\033[m\nJOGO EMPATADO')
elif a == 3 and jogador == 2:
    print('a maquina escolheu \033[31mtesoura\033[m\nO jogador escolheu \033[31mpapel\033[m\nisso é uma vitoria para a maquina')
elif a == 1 and jogador == 3:
    print('a maquina escolheu \033[31mpedra\033[m\nO jogador escolheu \033[31mtesoura\033[m\nisso é uma vitoria para a amaquina')
elif a == 2 and jogador == 3:
    print('a maquina escolheu \033[31mpapel\033[m\nO jogador escolheu \033[31mtesoura\033[m\nisso é uma vitoria para o jogador')
elif a == 3 and jogador == 3:
    print('a maquina escolheu \033[31mtesoura\033[m\nO jogador escolheu \033[31mtesoura\033[m\nJOGO EMPATADO')
else:
    print('numero invalido, tente denovo')