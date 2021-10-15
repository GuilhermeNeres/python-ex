#calculadora basica

from time import sleep
n = 1
while True:
    n = int(input('digite um numero '))
    if n < 0:
        break
    for c in range(0, 11):
        print(n,'x', c,f'= {n*c}')
        sleep(0.50)
print('Programa encerrado, volte sempre!')