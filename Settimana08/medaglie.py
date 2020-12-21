from pprint import pprint
from random import randint

counts = [
    [0, 3, 0],
    [0, 0, 1],
    [1, 2, 3],
    [2, 2, 2]
]

# counts è una lista (di 4 elementi) (che sono liste)
# counts[i] è una lista di 3 elementi (che sono interi)
# counts[i][j] è un intero

pprint(counts)

italia = counts[0]  # è un alias

print(italia)
italia[0] = 100
print(italia)
print(counts)

argento = []
for nazioni in counts:
    argento.append(nazioni[1])
print(argento)

righe = len(counts)
colonne = len(counts[0])  # ipotesi: le colonne sono tutte uguali / ciascuna lista contiene lo stesso numero di elementi
print(f'La tabella ha {righe} righe e {colonne} colonne')

# costruisco una nuova tabella con le stesse dimensioni, inizializzata con numeri casuali (0, 100)

tabella = []
for i in range(righe):
    # costruisci la riga numero i
    # riga = [ 0, 0, 0 ]
    riga = []
    for j in range(colonne):
        riga.append(randint(0, 100))
    # aggiungere alla tabella
    tabella.append(riga)

print(tabella)

# stampa la tabella

for riga in tabella:
    for col in riga:
        print(col, end=' ')
    print()

for i in range(righe):
    for j in range(colonne):
        print(tabella[i][j], end=' ')
    print()
