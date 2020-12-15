# Leggiamo l'elenco degli iscritti al corso
# dal file CSV della segreteria
# memorizzandoli come una lista di dizionari

# Ciascuno studente sarà rappresentato dai seguenti campi:
# cognome, nome, matricola, email  (gli altri non mi interessano)

# A partire dall'elenco degli studenti, determinare quale sia il nome
# più frequente nella classe

# Alla fine, stampare i primi 20 nomi in ordine decrescente di frequenza

from operator import itemgetter


def leggi_file(nome_file):
    studenti = []

    try:
        file = open(nome_file, 'r')
    except IOError:
        print('Errore: impossibile aprire il file')
        return []

    prima = True
    for line in file:
        if prima:
            prima = False
        else:
            campi = line.rstrip().split(',')
            record = {
                'cognome': campi[1],
                'nome': campi[2],
                'matricola': int(campi[0]),
                'email': campi[3]
            }
            studenti.append(record)

    file.close()
    return studenti


def estrai_lista_nomi(studenti):
    nomi = []
    for record in studenti:
        nomi.append(record['nome'])
    return nomi


# costruisci un dizionario che come CHIAVE ha il nome
# di uno studente e come VALORE ha il conteggio di
# quante volte quel come compare nella lista dei nomi

# Esempio: ['A','B', 'A', 'A', 'C', 'B'] --> { 'A': 3, 'B': 2, 'C': 1 }
def calcola_frequenza(nomi):
    frequenze = {}
    # le chiavi del dizionario sono i nomi UNICI della lista
    chiavi = set(nomi)
    for nome in chiavi:
        frequenza = nomi.count(nome)
        frequenze[nome] = frequenza
    return frequenze


def calcola_frequenza_bis(nomi):
    frequenze = {}

    for nome in nomi:
        if nome not in frequenze:
            # prima volta che lo vedo
            frequenze[nome] = 1
        else:
            frequenze[nome] = frequenze[nome] + 1

    return frequenze


def main():
    studenti = leggi_file('14BHDLZ_2021.csv')
    lista_nomi = estrai_lista_nomi(studenti)
    print(lista_nomi)
    frequenze = calcola_frequenza(lista_nomi)
    print(frequenze)
    max_frequenza = max(frequenze.values())
    print(max_frequenza)

    for (nome, freq) in sorted(frequenze.items()):
        if freq == max_frequenza:
            print(nome)

    lista_frequenze = []
    for (nome, freq) in frequenze.items():
        lista_frequenze.append({
            'nome': nome,
            'frequenza': freq
        })
    print(lista_frequenze)

    lista_frequenze.sort(key=itemgetter('frequenza'), reverse=True)

    print(lista_frequenze)

    for i in range(0, 20):
        print(f'{lista_frequenze[i]["nome"]} compare {lista_frequenze[i]["frequenza"]} volte')


main()
