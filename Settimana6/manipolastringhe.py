def inverti(parola):
    """
    Crea una nuova stringa pari a quella ricevuta, in ordine inverso (dall' ultimo carattere al primo)

    :param parola: stringa di partenza
    :return: stringa invertita
    """
    
    nuova = ''
    for ch in parola:
        nuova = ch + nuova

    # for i in range(len(parola)-1, -1, -1):
    #     nuova = nuova + parola[i]

    # nuova = parola[::-1]

    return nuova
