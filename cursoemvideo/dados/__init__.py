def leiadinheiro():
    while True:
        a = input('digite um numero ').strip()
        if a.isnumeric():
            from cursoemvideo import resumo
            a.replace('.', ',')
            a = float(a)
            resumo(a, a, a)
            break
        else:
            print('VALOR NAO RECONHECIDO! TENTE NOVAMENTE')

