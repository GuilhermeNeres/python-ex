lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceira = 0
maior = 0
terceiro = 0
for c in range(0, 3):
    for i in range(0, 3):
        numero = int(input(f'digite um numero para a posiçao {c}.{i} '))
        if numero % 2 == 0:
            pares += numero
        if i == 2:
            terceira += numero
        if maior == 0 and c == 1:
            maior = numero
        elif maior < numero and c == 1:
            maior = numero
        lista[c][i] = numero
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{lista[c][i]:^5}]', end='')
    print()
for c in range(0, 3):
    terceiro += lista[c][2]
mais = 0
for c in range(0, 3):
    if c == 0:
        mais = lista[1][c]
    elif lista[1][c] > mais:
        mais = lista[1][c]
paris = 0
for c in range(0, 3):
    for i in range(0, 3):
        if lista[c][i] % 2 == 0:
            paris += lista[c][i]
print(f'a soma dos valores pares é igual a {pares}')
print(paris)
print(f'a soma dos valores da terceira coluna é igual a {terceira}')
print(terceiro)
print(f'o maior valor da segunda linha é o {maior}')
print(mais)

