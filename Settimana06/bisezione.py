'''
Sia data una funzione reale di variabile reale y = f ( x ).
Si vuole trovare uno zero della funzione f nell'intervallo x ⋲ [a, b]
usando il metodo di bisezione (valido se f() è continua e f(a)f(b)<0)
'''

import math

EPSILON = 0.0000001


def main():
    print("Inserisci gli estremi dell'intervallo [a, b]")
    x1 = float(input("a="))
    x2 = float(input("b="))
    # zero = trovaZero(a=x1, b=x2)
    # zero = trovaZero(b=x2, a=x1)

    zero = trovaZero(x1, x2)
    # zero = trovaZero(x1, x2, eps=0.01)

    if zero is None:
        print('La funzione non cambia segno nell\'intervallo')
    else:
        print(f'La soluzione è {zero}')


def trovaZero(a, b, eps=EPSILON):
    """
    Ricerca di uno zero utilizzando il metodo di bisezione. Ricerca lo zero della funzione f(x)
    nell'intervallo [a, b].

    :param a: estremo sinistro dell'intervallo (compreso)
    :param b: estremo destro dell'intervallo (compreso)
    :param eps: (opzionale) precisione desiderata, l'algoritmo itera finché |a=b|<eps
    :return: migliore approssimazione troata per la soluzione
    """
    if f(a) * f(b) > 0:
        # hanno lo stesso segno -> non si può applicare
        return None  # valore "sentinella" per indicare l'anomalia
        # return "Errore"
    elif f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    else:
        # devo cercare!
        while abs(b - a) > eps:
            m = (a + b) / 2
            if f(m) == 0:
                return m
            elif f(m) * f(a) > 0:
                # f(m) ha il segno di f(a)
                a = m
            else:
                # f(m) ha il segno di f(b)
                b = m
        return m


def f(x):
    """
    Funzione in cui ricercare gli zeri
    """
    y = math.sin(x)
    return y


main()
