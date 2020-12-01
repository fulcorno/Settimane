"""
Scriviamo un programma per gestire un elenco di amici.

Il programma deve permetterci di inserire:
 - un singolo amico
 - un gruppo di amici (separati da virgola)

Ogni volta che un amico (o un gruppo) viene inserito dall'utente,
dovrà essere aggiunto ad una lista che memorizza tutti gli amici,
ma SOLO SE tale amico non esiste ancora (altrimenti si stampa un
messaggio di errore e si ignora il dato).

Ad ogni inserimento, il programma dovrà stampare il numero di amici presenti,
seguiti dall'elenco completo, in ordine alfabetico, con i nomi separati 
dal carattere ;

Il programma termina quando l'utente inserisce ***

OPZIONALE: qualora il nome di un amico (inserito da solo o come parte della lista),
sia nel formato "*Nome", allora si deve ELIMINARE l'amico con tale Nome.
"""


# Verifica che il nome fornito rispetti dei criteri di correttezza
def verifica_nome(nome):
    """
    Verifica che il nome rispetti dei criteri basilari di correttezza
    (non è stringa vuota, è fatto solo di lettere alfabetiche)

    :param nome: nome dell'amico inserito
    :return: True se il nome è corretto, False se non è corretto
    """
    if nome == '':
        return False
    elif not nome.isalpha():
        return False
    return True


# Dato un nome (fatto di caratteri alfabetici) lo converte in modo da
# avere l'iniziale maiuscola ed il resto minuscolo
def normalizza_maiuscole(nome):
    """
    Converte una stringa in modo da avere la lettera iniziale maiuscola e
    tutte le restanti lettere minuscole.

    :param nome: nome da convertire
    :return: nome convertito (str)
    """
    return nome[0].upper() + nome[1:].lower()


def inserisci_nome(nome, lista):
    """
    Aggiunge un nome ad una lista di nomi, se tale nome è valido e non esiste ancora.
    La lista dei nomi viene mantenuta sempre in ordine alfabetico.

    :param nome: nome da aggiungere
    :param lista: lista contenente l'elenco
    :return: Niente
    """
    if verifica_nome(nome):
        nome = normalizza_maiuscole(nome)

        # verifica che il nome non esista ancora
        if nome not in lista:
            # aggiungi il nome alla lista
            lista.append(nome)
            # mantieni l'ordine alfabetico
            lista.sort()

        else:  # nome è duplicato
            print(f"L'amico {nome} è già presente")
    else:      # verifica_nome fallisce
        print(f"Il nome {nome} non è scritto correttamente")


def main():
    amici = []

    linea = input('Inserisci un nome (*** per finire): ')
    while linea != '***':

        if ',' not in linea:
            # l'utente ha inserito un nome solo
            nome = linea
            inserisci_nome(nome, amici)
        else:
            # l'utente ha inserito un gruppo di nomi separati da ,
            # esempio: 'Qui,Quo,Qua' oppure 'AAAA, aaaa, Bccc, Dddd'

            # 1. dividi la 'linea' in corrispondenza delle ',' e metti i singoli nomi in una lista
            # 2. elimina gli spazi in eccesso rimasti nei singoli nomi
            nomi = linea.split(',')
            for i in range(0, len(nomi)):
                nomi[i] = nomi[i].strip()

            # 3. per ciascun nome, inseriscilo nella lista di amici
            for nome in nomi:
                inserisci_nome(nome, amici)

        # Voglio ottenere: elenco = amici[0]+';'+amici[1]+';' ecc...
        # elenco = ''
        # for i in range(0, len(amici)):
        #     elenco = elenco + amici[i] + ';'
        # elenco = elenco[:-1] # elimina l'ultimo carattere (; finale)
        elenco = ';'.join(amici)

        print(f'Hai {len(amici)} amici, sono: {elenco}')

        linea = input('Inserisci un nome (*** per finire): ')


# Esegui il programma principale
main()
