# Soluzione svolta in aula dell'esercizio sulle piastrelle

# DATI DI PARTENZA
PARETE = 3.20 # metri
LATO_PIASTRELLA = 0.15 # m

# Calcolare: N. piastrelle bianche, N. piastrelle nere, spazio vuoto ai lati
# Vincoli: prima e ultima piastrella sono nere, lo spazio è uguale ai due lati

# Calcola il numero di piastrelle

# La disposizione sarà questa
# | N BN BN BN BN BN |
# La prima piastrella è sempre nera
# poi rimane uno spazio pari a
spazioRimanente = PARETE - LATO_PIASTRELLA

# Lo spazio rimanente va riempito con coppie di piastrelle BN
numCoppieBN = int(spazioRimanente / (2*LATO_PIASTRELLA))

numeroPiastrelle = 1 + 2*numCoppieBN

print('Mi servono', numeroPiastrelle, 'piastrelle, di cui', numCoppieBN, 'bianche e',
      numCoppieBN+1, 'nere')

# Calcola lo spazio rimanente

spazioTotale = PARETE - LATO_PIASTRELLA*numeroPiastrelle
spazioPerLato = spazioTotale/2
print('Devi lasciare', round(spazioPerLato*100,2), 'cm ad ogni lato')
