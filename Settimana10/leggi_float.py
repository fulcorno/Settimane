# Lettura di un float da tastiera con gestione dell'errore

def leggi_float(msg, valmin=0.0, valmax=100.0):
    ok = False
    while not ok:
        try:
            num = input(msg)
            num = float(num)

            if valmin <= num <= valmax:
                ok = True
            else:
                print(f"Errore: il valore deve essere compreso tra {valmin} e {valmax}")
        except ValueError:
            print("Errore: Inserire un numero floating point nel formato corretto")

    return num


def main():
    a = leggi_float("Inserisci A: ")
    b = leggi_float("Inserisci B tra 10 e 20:", valmin=10.0, valmax=20.0)

    print(a, b)


main()
