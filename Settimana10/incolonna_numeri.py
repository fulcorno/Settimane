## Leggi ed in colonna i numeri

infile = open('numeri.dat', 'r')
outfile = open('risultato.dat', 'w')

riga = infile.readline()
somma = 0
conta = 0
while riga != '':
    # elabora
    num = float(riga)
    outfile.write(f'{num:8.2f}\n')
    somma = somma + num
    conta = conta + 1

    riga = infile.readline()

# aggiungi i dati finale
outfile.write('-'*10+'\n')
outfile.write(f'La somma vale {somma}\n')
outfile.write(f'La media vale {somma/conta}\n')



infile.close()
outfile.close()
