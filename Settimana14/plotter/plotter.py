LATO_RIQUADRO = 20
FILE_PLOTTER = 'plotter.txt'


def crea_riquadro(lato):
    riquadro = []
    for i in range(lato):
        riga = ['.'] * lato
        riquadro.append(riga)
    return riquadro

'''
1) leggo tutto il file plotter.txt, memorizzo le informazioni in una lista , e successivamente leggo la lista e disegno le figure
2) leggo il file una riga per volta, e per ogni riga eseguo subito l'operazione
'''

def disegna(line, riquadro):
    # analizza il comando ricevuto
    campi = line.rstrip().split()
    if len(campi)<3:
        print('Numero di campi insufficiente')
        return
    op = campi[0].upper()
    try:
        x = int(campi[1])
        y = int(campi[2])
        if op=='H' or op=='V':
            lun = int(campi[3])
    except ValueError:
        print('Errore nel formato dei campi numerici')
        return
    except IndexError:
        print('Numero di campi insufficiente')
        return

    #if x<0 or y<0 or x>=LATO_RIQUADRO or y>=LATO_RIQUADRO:
    if not( 0<=x<LATO_RIQUADRO and 0<=y<LATO_RIQUADRO):
        print('Coordinate fuori dal riquadro')
        return

    # per ora funziona se il file è corretto
    # TODO: aggiungere controlli sulla lettura dei dati

    if op=='P':
        # riquadro[LATO_RIQUADRO-y-1][x] = '*'
        riquadro[y][x] = '*'  ## uso riga==y, e ricordo che dovrò stampare la matrice dall'ultima riga alla prima
    elif op=='H':
        if lun<=0 or x+lun>LATO_RIQUADRO:
            print('Valore di lunghezza non valido')
            return
        for x1 in range(x, x+lun):
            if riquadro[y][x1]=='|': # or riquadro[y][x1]=='+':
                riquadro[y][x1] = '+'
            else:
                riquadro[y][x1] = '-'
    elif op=='V':
        if lun<=0 or y+lun>LATO_RIQUADRO:
            print('Valore di lunghezza non valido')
            return
        for y1 in range(y, y+lun):
            if riquadro[y1][x] == '-':
                riquadro[y1][x] = '+'
            else:
                riquadro[y1][x] = '|'
    else:
        print(f'Operazione {op} non valida')



    # modifica il riquadro in funzione del comando


def stampa_riquadro(riquadro):
    for riga in range(len(riquadro)-1, -1, -1):
        print(''.join(riquadro[riga]))


def main():
    riquadro = crea_riquadro(LATO_RIQUADRO)

    try:
        comandi = open(FILE_PLOTTER, 'r')
    except IOError:
        print('Impossibile aprire il file '+FILE_PLOTTER)
        exit()

    for line in comandi:
        disegna(line, riquadro)

    comandi.close()

    stampa_riquadro(riquadro)

main()

