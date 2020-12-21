import math


# calcola il volume di un solido che è composto da un cubo di lato 'side'
# su cui è appoggiato un cilindro di diametro di base 'side' ed altezza
# ancora 'side'
def compositeVolume(side):
    vol1 = cubeVolume(side)
    vol2 = cylinderVolume(side / 2, side)
    return vol1 + vol2


def cubeVolume(sideLength):
    '''
    Calcola il volume di un cubo dato il lato

    :param sideLength: lungnezza del lato
    :return: volume del cubo
    '''
    volume = sideLength ** 3
    return volume


def cylinderVolume(baseRadius, heigth):
    areaBase = math.pi * baseRadius ** 2
    volume = areaBase * heigth
    return volume


def areaVolumeCube(sideLength):
    area = sideLength ** 2
    volume = cubeVolume(sideLength)
    return (area, volume)


# il programma principale inizia da qui

lato = 3.5

(a, v) = areaVolumeCube(lato)
x = areaVolumeCube()
print(a)
print(v)
print(f'L\'area vale {a} ed il volume vale {v}')

solido = cubeVolume(lato)
print(f'Il volume del cubo di lato {lato} è pari a {solido}')

solido = cylinderVolume(lato, 2.5)
print(f'Il volume del cilindro è pari a {solido}')

solido = compositeVolume(lato)
print(f'il volume del solido strano è pari a {solido}')

altroLato = 77
solido = cubeVolume(altroLato)
print(f'Il volume del cubo di lato {altroLato} è pari a {solido}')

# Calcola la somma dei cubi dei numeri da 1 a 100
somma = 0.0
for lato in range(1, 101):
    somma = somma + cubeVolume(lato)
print(f'La somma dei cubi dei primi 100 numeri è {somma}')
