# L'utente inserisce un dato, il programma lo visualizza e dice di che tipo di dato si tratta

dato = input("Inserisci qualcosa: ")

print("Hai inserito: ", dato)
print("Ha lunghezza: ", len(dato))
print("Mi piace....\n", dato*5)

if dato.isnumeric():
    valore = int(dato)
    print("Il valore intero è: ", valore)
