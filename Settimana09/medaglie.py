COUNTRIES = 8
MEDALS = 3

country_names = ['Canada', 'Italia', 'Germania', 'Giappone', 'Kazakistan', 'Russia',
                 'Corea del Sud', 'USA']

medal_names = ['Oro', 'Argento', 'Bronzo']

# Medaglie vinte.
# La cella counts[n][m] riporta il numero di medaglie di tipo medal_names[m]
# vinte dalla nazione country_names[n]
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 1, 0]
]

'''
ESERCIZIO 0:
Stampare quale NAZIONE ha ottenuto il numero MASSIMO di medaglie totali, e quale ha ottenuto
il numero MINIMO.

ESERCIZIO 1:
Permettere all'utente di inserire una NAZIONE, e stampare per quella nazione
1) il numero di medaglie totali vinte (di tutti i tipi)
2) quale tipo di medaglia è stata vinta di più dalla nazione
3) il numero di medaglie per ciascun tipo.

ESERCIZIO 2:
Permettere all'utente di inserire un TIPO DI MEDAGLIA, e stampare per quella medaglia
1) il numero di medaglie totali vinte (su tutte le nazioni)
2) quale nazione ha vinto il massimo numero di medaglie di quel tipo
3) il numero di medaglie di quel tipo vinte da ciascuna nazione.

ESERCIZIO 3: (provate a pensarci!)
Stampare l'elenco delle nazioni, ordinate per numero decrescente di medaglie TOTALI
'''


def main():
    print("*** Medagliere Olimpico ***")

    esci = False

    while not esci:
        print('''Opzioni:
 M - Nazione con massimo e minimo numero di medaglie
 N - Ricerca per nazione
 T - Ricerca per tipo di medaglia
 C - Classifica in ordine
 * - Esci''')
        scelta = input('Scelta (NMTC*): ')
        scelta = scelta.upper()

        if scelta == 'M':
            min_max_medaglie(counts, country_names)
        elif scelta == 'N':
            ricerca_per_nazione(counts, country_names, medal_names)
        elif scelta == 'T':
            ricerca_per_medaglia(counts, country_names, medal_names)
        elif scelta == 'C':
            print("😐 non ancora implementato")
        elif scelta == '*':
            esci = True
        else:
            print("Comando errato")


# count ha 8 righe e 3 colonne
# numero di righe: len(counts)
# numero di colonne: len(counts[0])

def min_max_medaglie(counts, country_names):
    """
    Stampa quale NAZIONE ha ottenuto il numero MASSIMO di medaglie totali, e quale ha ottenuto
il numero MINIMO.

    :param counts: tabella con il numero di medaglie
    :param country_names: lista con i nomi delle nazioni (una nazione ogni riga della tabella)
    :return: niente
    """
    # trova il massimo del valore Oro+Argento+Bronzo
    maxMedaglie = 0
    maxNazione = ''
    minMedaglie = 9999
    minNazione = ''
    for nazione in range(len(counts)):
        # medaglie_totali = counts[nazione][0] + counts[nazione][1] + counts[nazione][2]

        # medaglie_totali = 0
        # for num in counts[nazione]:
        #     medaglie_totali = medaglie_totali + num

        medaglie_totali = sum(counts[nazione])

        if medaglie_totali > maxMedaglie:
            maxMedaglie = medaglie_totali
            maxNazione = nazione
        if medaglie_totali < minMedaglie:
            minMedaglie = medaglie_totali
            minNazione = nazione
    print(f'Massimo numero di medaglie: {maxMedaglie} vinte da {country_names[maxNazione]}')
    print(f'Minimo  numero di medaglie: {minMedaglie} vinte da {country_names[minNazione]}')


def ricerca_per_nazione(counts, country_names, medal_names):
    """
    Permette all'utente di inserire una NAZIONE, e stampa per quella nazione
1) il numero di medaglie totali vinte (di tutti i tipi)
2) quale tipo di medaglia è stata vinta di più dalla nazione
3) il numero di medaglie per ciascun tipo.

    :param counts: tabella con il numero di medaglie
    :param country_names: lista con i nomi delle nazioni (una nazione ogni riga della tabella)
    :param medal_names: lista con i nomi delle medaglie (una medaglia ogni colonna della tabella)
    """
    nomeNazione = input("Nazione: ")
    if nomeNazione in country_names:
        # nome nazione giusto
        riga = country_names.index(nomeNazione)
        mieMedaglie = counts[riga]
        # counts[riga] è una LISTA che contiene i valori della riga numero 'riga'
        # per comodità assegno un alias 'mieMedaglie' a tale riga
        # print(f'Riga {riga}')
        print(f'Medaglie totali di {nomeNazione}: {sum(mieMedaglie)}')

        # trovo la medaglia vinta di più
        posMax = 0
        for pos in range(1, len(mieMedaglie)):
            if mieMedaglie[pos] > mieMedaglie[posMax]:
                posMax = pos
        print(f'La medaglia più vinta è {medal_names[posMax]}')

        # stampo le medaglie per ogni tipo
        for pos in range(0, len(mieMedaglie)):
            print(f'{medal_names[pos]}={mieMedaglie[pos]}   ', end='')
        print()

    else:
        print("Nome nazione errato")


def ricerca_per_medaglia(counts, country_names, medal_names):
    """
    Permette all'utente di inserire un TIPO DI MEDAGLIA, e stampa per quella medaglia
1) il numero di medaglie totali vinte (su tutte le nazioni)
2) quale nazione ha vinto il massimo numero di medaglie di quel tipo
3) il numero di medaglie di quel tipo vinte da ciascuna nazione.

    :param counts: tabella con il numero di medaglie
    :param country_names: lista con i nomi delle nazioni (una nazione ogni riga della tabella)
    :param medal_names: lista con i nomi delle medaglie (una medaglia ogni colonna della tabella)
    """
    nomeMedaglia = input("Medaglia: ")
    if nomeMedaglia in medal_names:
        # nome medaglia giusto
        colonna = medal_names.index(nomeMedaglia)
        # medaglie per nazione = counts[nazione][colonna]

        sumMedaglie = 0
        for nazione in range(len(country_names)):
            sumMedaglie = sumMedaglie + counts[nazione][colonna]
        print(f'Medaglie totali di {nomeMedaglia}: {sumMedaglie}')

        # trovo la nazione che vinto di più
        posMax = 0
        for pos in range(1, len(country_names)):  # pos -> nazione (==riga)
            if counts[pos][colonna] > counts[posMax][colonna]:
                posMax = pos
        print(f'La nazione che ha più {nomeMedaglia} è {country_names[posMax]}')

        # stampo le medaglie per ogni nazione
        for pos in range(0, len(country_names)):
            print(f'{country_names[pos]}={counts[pos][colonna]}   ', end='')
        print()

    else:
        print("Nome medaglia errato")


main()
