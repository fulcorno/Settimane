# soluzione esercizio "gelati"
from pprint import pprint

NOME_FILE = 'icecream.txt'

# La struttura dati utilizzata sarà un dizionario che ha
#  chiave -> stringa -> gusto del gelato
#  valore -> lista di numeri reali -> vendite dei 3 negozi (in ordine)

def leggi_file(nome_file):
    gelati = {}
    infile = open(nome_file, 'r')
    for line in infile:
        campi = line.rstrip().split(':')
        gusto = campi[0]
        valori = []
        for i in range(1, len(campi)):
            valori.append(float(campi[i]))
        gelati[gusto] = valori
        num_negozi = len(valori)
    infile.close()
    return gelati, num_negozi


def stampa_tabella(gelati, num_negozi):
    # inzizalizza i totali per negozio [0, 0, 0]
    tot_negozio = [ 0.0 ] * num_negozi    #  len(list(gelati.values())[0])    # len(gelati[list(gelati.keys())[0]]))

    # stampa la tabella per gusto
    for gusto in sorted(gelati):
        tot_gusto = sum(gelati[gusto])  # somma di riga

        print(f'{gusto:15s}', end='')  # stampa il gusto (prima colonna)
        for i in range(len(gelati[gusto])):  # stampa gli incassi dei 3 negozi
            vendita = gelati[gusto][i]  # incasso i-esimo negozio per questo gusto
            print(f'{vendita:15.2f}', end='')
            tot_negozio[i] = tot_negozio[i] + vendita   # aggiorna il totale dell'i-esimo negozio per tutti i gusti
        print(f'{tot_gusto:20.2f}')   # stampa totale di riga (di gusto)

    # ultima riga
    print(' '*15, end='')
    for tot in tot_negozio:
        print(f'{tot:15.2f}', end='')
    print()


gelati, num_negozi = leggi_file(NOME_FILE)
# pprint(gelati, sort_dicts=False)
stampa_tabella(gelati, num_negozi)
