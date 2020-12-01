# Acquisire una serie di numeri reali dall'utente
# e stampare la somma di essi (ed il valor medio)
# Non si sa a priori quanti dati verranno inseriti

# Se l'utente inserisce "*" l'inserimento termina

totale = 0.0
count = 0
fine = False

while not fine:
    dato = input("Dato (* per finire): ")
    # dato -> stringa

    if dato == '*':
        fine = True
    else:
        # caso normale
        dato = float(dato)
        totale = totale + dato
        count = count + 1

print(f'Il totale vale {totale}')
if count>0:
    print(f'La media vale {totale/count}')
