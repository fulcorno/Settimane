''''
Costruire una funzione che, data una stringa passata in input,
restituisca la stessa stringa in ordine inverso
(esempio: gatto -> ottag)

Bonus: gatto -> oʇʇɐƃ  (v. http://www.upsidedowntext.com/)
'''
from manipolastringhe import inverti


# Programma principale
def main():
    testo = input('Inserisci una parola: ')
    testoInvertito = inverti(testo)
    print(f'La parola {testo} al contrario si legge {testoInvertito}')


# esegue il programma
main()
