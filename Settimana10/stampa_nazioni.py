# Leggi ed analizza il file 'rawdata_2004.txt'

FILENAME = 'rawdata_2004.txt'

infile = open(FILENAME, 'r')

for riga in infile:
    numero = int(riga[:6])
    nome = riga[7:7+50].strip()
    valore = riga[58:].strip()
    print(f'{numero}:{nome}:{valore}')

infile.close()
