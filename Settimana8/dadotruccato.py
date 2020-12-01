# controlla se un dato è truccato

def main():
    # legge una serie di 'lanci'
    lanci = leggi_lanci()

    # lanci: una lista che contiene i valori usciti dal dado: ciascun elemento della lista sarà un valore tra 1 e 6
    # es: [1, 5, 3, 4, 2, 1, 6, 6, 2, 2 ]

    # calcola la frequenza dei vari lanci
    frequenze = calcola_frequenze(lanci)
    # frequenze è una lista, in cui nella posizione 'i' è contenuto il numero
    # di volte in cui è uscita la faccia 'i'
    # es: [0, 2, 3, 1, 1, 1, 2]
    # è una LISTA DI CONTATORI

    for faccia in range(1, 7):
        print(f'La faccia {faccia} è uscita {frequenze[faccia]} volte')


def leggi_lanci():
    lanci = []
    # STUB return [1, 5, 3, 4, 2, 1, 6, 6, 2, 2 ]  # faccio finta che l'utente abbia inserito questi numeri
    dado = input("Inserisci il valore del dato (1-6, * per uscire): ")
    while dado != '*':
        if dado.isdigit():
            valore = int(dado)
            if 1 <= valore <= 6:
                # valore corretto
                lanci.append(valore)
            else:
                print(f'Valore {valore} non valido')
        else:
            print(f'Dato {dado} non numerico')

        dado = input("Inserisci il valore del dato (1-6, * per uscire): ")
    return lanci


def calcola_frequenze(lanci):
    # crea una lista di 6 contatori
    freq = [0, 0, 0, 0, 0, 0, 0]  # oppure [0]*7
    for lancio in lanci:
        freq[lancio] = freq[lancio] + 1  # prendi una cella della lista ed incrementala di 1
        # NO!! freq[lancio] = freq[lancio+1]  # freq[2]=freq[3] -> copia un valore da una cella a quella precedente
    return freq


main()
