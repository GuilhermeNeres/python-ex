lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0,3):
    for i in range(0,3):
        numero = int(input('digite um numero '))
        lista[c][i] = numero
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{lista[c][i]:^5}]', end='')
    print()
