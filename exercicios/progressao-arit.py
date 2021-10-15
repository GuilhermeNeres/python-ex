#progressão arritmetica
from time import sleep
print('sera mostrado a progressão aritmetica pro numero digitado')
razao = int(input('digite a razão da progressão '))
termo = int(input('digite o primeiro termo da progressão '))
n = termo * 11
from time import sleep
print('está sendo feito o calculo...')
sleep(2)
if termo == 0:
    n = razao * 10
    for c in range(termo, n, razao):
        print(c)
        sleep(0.25)
elif razao == 0:
    for c in range (termo, n):
        print(c)
        sleep(0.25)
else:
    for c in range(termo, n, razao):
        print (c)
        sleep(0.25)
