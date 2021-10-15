#diz se uma frase é palindromo ou nao

frase = str(input('digite uma frase ')).strip().split()  # aqui eu dei strip, pra tirar espaço da frente e de tras, split pra botar numa lista
frasee = ''.join(frase)  # aqui eu juntei a frase sem os espaços
frase2 = frasee[::-1]  # aqui foi botado a frase ao contrario
if frasee == frase2:
    print('a frase digitada é um palindromo')
else:
    print('A frase digitada não é um palindromo')
print(frasee)
print(frase2)

