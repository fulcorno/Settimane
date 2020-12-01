# Stampa a video, una per riga, le parole del testo della filastrocca

FILENAME = 'mary.txt'

mary = open(FILENAME, 'r')

for riga in mary:
    parole = riga.rstrip().split()
    for parola in parole:

        print(parola.rstrip(',.;:?'))

mary.close()


# while not parola[-1].isalpha():
#     parola = parola[:-1]
