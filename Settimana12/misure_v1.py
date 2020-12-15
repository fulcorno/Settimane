# Vogliamo memorizzare la temperatura presa a diverse persone
# È possibile che una persona misuri la temperatura più di una volta
# e vogliamo ricordarci tutte le misure prese

"""
**** VERSIONE UNO: UNA PERSONA -> UNA SOLA TEMPERATURA ****
"""

def main():

    misure = {}

    nome = input('Nome della persona (* per terminare): ')
    if nome!='*':
        temp = float(input('Misura della temperatura: '))

    while nome != '*':
        # aggiungi nome, temp ai dati
        misure[nome] = temp

        print(misure)

        nome = input('Nome della persona (* per terminare): ')
        if nome!='*':
            temp = float(input('Misura della temperatura: '))


main()
