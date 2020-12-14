# Creare un programma che analizzi i testo presente nel libro 'story.txt' e mi stampi le parole che lessicalmente
# sono scorrette (non compaiono nell'elenco 'parole')

FILE_PAROLE = 'parole'
FILE_STORIA = 'story.txt'

# dizionario = un insieme contente tutte le parole del dizionario
#
# storia = insieme contenente tutte le parole della storia
#
# se non ci sono errori => storia è un sottoinsieme del dizionario
# se ci sono errori => errori = storia - dizionario

# Dato il nome di un file, restituisce un **insieme** che contiene le parole uniche presenti nel file
# Attenzione: rimuove tutti i segni di punteggiatura
def parole_uniche(nome_file):
    try:
        file = open(nome_file, 'r')
    except IOError:
        print(f"Errore nell'apertura del file {nome_file}")
        exit()

    insieme = set()

    for line in file:
        parole = line.rstrip().replace('-', ' ').split()
        for parola in parole:
            parola_pulita = pulisci(parola)
            if parola_pulita!='':
                insieme.add(parola_pulita.lower())

    file.close()
    return insieme

# rimuove tutti i caretteri INIZIALI e FINALI non alfabetici da una stringa
def pulisci(parola):
    pulita = parola

    while len(pulita)>0 and not pulita[0].isalpha():
        pulita = pulita[1:]

    while len(pulita)>0 and not pulita[-1].isalpha():
        pulita = pulita[:-1]

    return pulita


def main():
    dizionario = parole_uniche(FILE_PAROLE)
    # print(dizionario)

    storia = parole_uniche(FILE_STORIA)

    if storia.issubset(dizionario):
        print("La storia non ha errori lessicali")
    else:
        parole_sbagliate = storia.difference(dizionario)
        print("Le parole sbagliate sono:")
        # print(parole_sbagliate)
        print(sorted(parole_sbagliate))

main()
