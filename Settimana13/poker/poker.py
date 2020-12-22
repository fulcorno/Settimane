# Soluzione svolta insieme dell'esercizio 'Poker'

# Come rappresentare il Mazzo di 32 carte o la Mano di 5 carte -> Lista

# Come rappresentare ciascuna singola carta?

# # stringa
# carta = "10C"
# carta = "7P"
# seme = carta[-1]
# valore = carta[:-1]
#
# # tupla
# carta = ('8', 'P')
# carta = ('10', 'F')
# seme = carta[1]
# valore = carta[0]
#
# # dizionario usato come 'record'
# carta = {
#     'valore': '8',
#     'seme': 'P'
# }
# carta = {
#     'valore': '10',
#     'seme': 'F'
# }
# valore = carta['valore']
# seme = carta['seme']

from pprint import pprint
from random import shuffle, randint

VALORI = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SEMI = ['P', 'F', 'Q', 'C']


def crea_mazzo():
    mazzo = []
    for valore in VALORI:
        for seme in SEMI:
            carta = {
                'valore': valore,
                'seme': seme
            }
            mazzo.append(carta)
    return mazzo


# riordina le carte nella lista (non crea una nuova lista)
def mescola_mazzo(mazzo):
    # shuffle(mazzo)
    copia = list(mazzo)
    mazzo.clear()   # mazzo[:] = []
    while len(copia)>0: # ci sono ancora carte da prendere
        pos = randint(0, len(copia)-1)
        mazzo.append(copia[pos])
        copia.pop(pos)

def salva_mazzo(nomefile, mazzo):
    outfile = open(nomefile, 'w')
    for carta in mazzo:
        outfile.write(f'{carta["valore"]} {carta["seme"]}\n')
    outfile.close()


def estrai_mani(mazzo):

    while len(mazzo)>=5:
        mano = mazzo[0:5]

        del mazzo[0:5]

        # mazzo[0:5] = []
        # mazzo[:] = mazzo[5:]
        # for i in range(0,5):
        #    mazzo.pop(0)

        # ERRORE
        # for i in range(0,5):
        #     mazzo.pop(i)

        # attenzione: rompe l'alias (non è vietato, ma devo saperlo) mazzo = mazzo[5:]

        for carta in mano:
            print(f'{carta["valore"]:>2s}-{carta["seme"]} ', end='')
        print(combinazione(mano))


def combinazione(mano):
    if is_scala(mano) and is_colore(mano):
        return 'Scala reale'
    elif has_uguali(mano, 4):
        return 'Poker'
    elif is_colore(mano):
        return 'Colore'
    elif has_uguali(mano, 3) and has_uguali(mano, 2):
        return 'Full'
    elif is_scala(mano):
        return 'Scala'
    elif has_uguali(mano, 3):
        return 'Tris'
    elif is_doppia_copia(mano):
        return 'Doppia coppia'
    elif has_uguali(mano, 2):
        return 'Coppia'
    else:
        return 'Carta singola'


def is_colore(mano):
    semi = set()
    for carta in mano:
        semi.add(carta['seme'])
    if len(semi)==1:
        return True
    else:
        return False


# questa mano ha esattamente 'tot' carte uguali??
def has_uguali(mano, tot):
    valori = []
    for carta in mano:
        valori.append(carta['valore'])
    # ['K', '10', 'A', 'Q', 'K']

    for valore in valori:
        if valori.count(valore) == tot:
            return True

    return False


def is_scala(mano):
    return False

def is_doppia_coppia(mano):
    return False

mazzo = crea_mazzo()

mescola_mazzo(mazzo) # mescola il mazzo che ti passo come parametro
# ALTRA POSSIBILITÀ:  mazzo = mescola_mazzo(mazzo) # riceve un mazzo e ne restituisce uno diverso, mescolato
salva_mazzo('mazzo.txt', mazzo)

estrai_mani(mazzo)
# pprint(mazzo, sort_dicts=False)
