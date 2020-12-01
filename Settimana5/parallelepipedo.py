'''
Scriviamo un programma per calcolare il volume di un parallelepipedo.
Il programma dovrà acquisire le dimensioni dei tre lati (che devono essere positive e <1000.0)
e poi stampare il volume calcolato.
Nel caso in cui l'utente inserisca il valore di un lato non valido, deve essere ripetuto
l'inserimento.
'''

LATI = 3

volume = 1.0
for i in range(LATI):

    # Legge un lato e garantisce che sia compreso tra 0 e 1000
    lato = float(input(f'Lato {i+1}: '))
    while lato<=0.0 or lato >=1000.0:
        print(f'Valore {lato} non valido, ripeti')
        lato = float(input(f'Lato {i+1}: '))

    volume = volume * lato

print(f'Il volume è pari a {volume}')
