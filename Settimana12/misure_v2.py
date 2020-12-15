# Vogliamo memorizzare la temperatura presa a diverse persone
# È possibile che una persona misuri la temperatura più di una volta
# e vogliamo ricordarci tutte le misure prese

"""
**** VERSIONE DUE: UNA PERSONA -> MOLTE MISURE DI TEMPERATURA ****
"""

def main():

    misure = {}

    nome = input('Nome della persona (* per terminare): ')
    if nome!='*':
        temp = float(input('Misura della temperatura: '))

    while nome != '*':
        # aggiungi nome, temp ai dati
        if nome not in misure:
            # persona nuova, la prima misura ricevuta
            misure[nome] = [temp]
        else:
            misure[nome].append(temp)

        # print(misure)
        for n in misure:
            print(n, misure[n])

        for (n, t) in misure.items():
            print(n, t)

        nome = input('Nome della persona (* per terminare): ')
        if nome!='*':
            temp = float(input('Misura della temperatura: '))


main()
