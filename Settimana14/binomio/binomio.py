# import

# costanti

def tartaglia(N):
    triangolo = [ [1] ]
    for i in range(1,N+1):
        riga = [1]
        for j in range(1,i):
            # creo la casella [i][j] del triangolo, sommando la [i-1][j] con [i-1][j-1]
            valore = triangolo[i-1][j] + triangolo[i-1][j-1]
            riga.append(valore)
        riga.append(1)

        triangolo.append(riga)
    return triangolo

    # [1] i=0
    # [1, 1] i=1
    # [1, 2, 1] i=2
    # [1, 3, 3, 1] i=3
    # [1, 4, 6, 4, 1] i = 4


def coefficienti(a, b, N):
    # calcola una lista di float contenente i coefficienti di (ax+by)^N
    # [ coeff di x^n, coeff di xN-1 y, coeff di xN-2 y2, ... ]
    # l'indice nella lista è la potenza di y
    # la potenza di x sarà N-indice

    triangolo = tartaglia(N)

    coeff = []
    for i in range(0, N+1):
        coeff.append( a**(N-i) * b**i * triangolo[N][i])
    return coeff


def main():
    try:
        comandi = open('potenze.txt', 'r')
    except IOError:
        print('Impossibile aprire il file')
        exit()

    riga = comandi.readline()
    a = float(riga.rstrip().split()[0])
    b = float(riga.rstrip().split()[1])

    print(f'Potenze di ({a}x + {b}y)^N')

    for line in comandi:
        N = int(line)
        coeff = coefficienti(a, b, N)
        stampa_polinomio(coeff)

    comandi.close()


def stampa_polinomio(c):
    # calcola una stringa contente la rappresentaione del polinomio
    s = ''
    N = len(c)-1
    for i in range(len(c)):
        # s = s + f'{c[i]} x^{N-i} y^{i} + '
        s += f'{c[i]}'

        if N-i == 1:
            s += ' x'
        elif N-i > 1:
            s += f' x^{N-i}'

        if i == 1:
            s += ' y'
        elif i > 1:
            s += f' y^{i}'

        if i!=N:
            s += ' + '
    print(s)


main()
