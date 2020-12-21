saldo_iniziale = 10000
interesse = 0.05

# inizializzare le variabili usate nel ciclo -> valori usati alla PRIMA ITERAZIONE
anno = 0
saldo = saldo_iniziale


while saldo < saldo_iniziale*2 :
    # corpo del ciclo: cosa deve essere ripetuto
    saldo = saldo + saldo * interesse
    anno = anno + 1

print(f'Dopo {anno} anni il saldo sarà {saldo}')
