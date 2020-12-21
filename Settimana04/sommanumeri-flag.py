# Acquisire una serie di numeri reali dall'utente
# e stampare la somma di essi (ed il valor medio)
# Non si sa a priori quanti dati verranno inseriti

# Si assuma che i dati da inserire siano tutti >=0
# Un valore negativo inserito identifica il termine
# dell'inserimento dei dati da parte dell'utente

totale = 0.0
count = 0
fine = False
#continua = True

# while continua: # ci_sono_ancora_dati

while not fine:
    dato = float(input("Dato (-1 per finire): "))

    if dato < 0:
        # valore 'sentinella' -> l'utente vuole terminare
        fine = True
        # continua = False
    else:
        # caso normale
        totale = totale + dato
        count = count + 1

print(f'Il totale vale {totale}')
if count>0:
    print(f'La media vale {totale/count}')
