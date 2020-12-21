# Risoluzione "indice analitico"

# memorizziamo i dati in un "dizionario di insiemi"

FILE_TERMINI = 'indexdata.txt'
FILE_INDICE = 'analitico.txt'


def leggi_termini():
    entries = {}
    infile = open(FILE_TERMINI, 'r')

    for line in infile:
        campi = line.rstrip().split(':')
        n_pag = int(campi[0])
        termine = campi[1]

        if termine in entries:
            # c'è già, aggiungo la pagina al set già esistente
            entries[termine].add(n_pag)
        else:
            # è la prima volta che vedo il termine, devo creare la nuova entry
            entries[termine] = { n_pag }  # insieme che contiene un elemento che è un intero
            # entries[termine] = set()
            # entries[termine].add(n_pag)

    infile.close()
    return entries


def scrivi_indice(entries):
    outfile = open(FILE_INDICE, 'w')

    for termine in sorted(entries):
        outfile.write(f"{termine}: ")
        numeri = sorted(entries[termine])

        # prima = True
        # for n in numeri:
        #     if not prima:
        #         outfile.write(', ')
        #     outfile.write(str(n))
        #     prima = False
        # outfile.write('\n')

        numeriS = []
        for n in numeri:
            numeriS.append(str(n))
        outfile.write( ', '.join(numeriS) + '\n' )


    # for (k,v) in sorted(entries.items()):
    #     outfile.write(f'{k}: ')
    #     for n in sorted(v):
    #         outfile.write(f'{n}; ')
    #     outfile.write('\n')


    outfile.close()


def main():
    entries = leggi_termini()
    # print(entries)

    scrivi_indice(entries)

main()
