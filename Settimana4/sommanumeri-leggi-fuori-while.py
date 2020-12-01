# Acquisire una serie di numeri reali dall'utente
# e stampare la somma di essi (ed il valor medio)
# Non si sa a priori quanti dati verranno inseriti

# Si assuma che i dati da inserire siano tutti >=0
# Un valore negativo inserito identifica il termine
# dell'inserimento dei dati da parte dell'utente

totale = 0.0
count = 0

dato = float(input("Dato (-1 per finire): ")) # primo dato

while dato != -1:
    # caso normale
    totale = totale + dato
    count = count + 1

    dato = float(input("Dato (-1 per finire): ")) # dato successivo

print(f'Il totale vale {totale}')
if count>0:
    print(f'La media vale {totale/count}')
