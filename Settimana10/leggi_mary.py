## Leggiamo le prime righe di mary.txt
## e creiamo il file mary2.txt che ne contiene una COPIA
## solo dei primi 10 caratteri di ogni linea
## tutta convertita in maiuscolo

mary = open('mary.txt', 'r')
out_mary = open('mary2.txt', 'w')


print('-'*20)

riga = mary.readline()  # leggi prima riga
while riga != '':
    riga = riga.rstrip()
    riga = riga.upper()
    riga = riga[:10]
    out_mary.write(riga+'\n')

    riga = mary.readline()  # leggi riga successiva

print('-'*20)

mary.close()
out_mary.close()
