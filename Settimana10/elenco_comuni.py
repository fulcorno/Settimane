# Stampa l'elenco dei comuni italiani

FILENAME = 'comuni_italiani.txt'

infile = open(FILENAME, 'r', encoding='utf-8')

# infile.readline()  # leggi e scarta la prima riga

comuni = []

prima = True  # sono sulla prima riga?
for riga in infile:
    if prima:
        prima = False
    else:
        campi = riga.rstrip().split(';')
        comuni.append(campi[5])

infile.close()

print(comuni)
