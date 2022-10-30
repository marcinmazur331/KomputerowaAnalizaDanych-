import math

sepalLenght = []
sepalWidth = []
petalLength = []
petalWidth = []
species = []
with open('test.csv', 'r') as file:
    size = 0
    for line in file:
        size += 1
        container = line.split(',')
        sepalLenght.append(float(container[0]))
        sepalWidth.append(float(container[1]))
        petalLength.append(float(container[2]))
        petalWidth.append(float(container[3]))
        if container[4] == "0\n":
            species.append("setosa")
        if container[4] == "1\n":
            species.append("versicolor")
        if container[4] == "2\n":
            species.append("virginica")


def liczebnosc(nazwa):
    counter = 0
    for i in species:
        if species[i] == nazwa:
            counter += 1
    return counter


def udzial_procentowy(nazwa):
    return round(liczebnosc(nazwa) / size, 2)


def maksimum(*cecha):
    max = -1
    for i in range(size):
        if cecha[i] > max:
            max = cecha[i]
    return max


def minimum(*cecha):
    min = 1000
    for i in range(size):
        if cecha[i] < min:
            min = cecha[i]
    return min


def srednia_arytmetyczna(*cecha):
    suma = 0
    for i in range(size):
        suma += cecha[i]
    return suma / size


def mediana(*cecha):
    # sortowanie!
    if size % 2 == 0:
        return round((cecha[int(size / 2)] + cecha[(int(size / 2)) + 1]) / 2, 2)
    return cecha[int(size / 2) + 1]


def kwartyl(*cecha):
    # sortowanie!
    array1 = []
    array2 = []
    if size % 2 == 0:
        for i in range(int(size/2)):
            array1[i] = cecha[i]
        for i in range(int(size/2) + 1, size):
            array2[i] = cecha[i]
        dolny = mediana(array1)
        gorny = mediana(array2)
        return (dolny, gorny)
    for i in reversed(range(int(size/2))):
        array1[i] = cecha[i]
    for i in range(math.floor(size/2)+1, size):
        array2[i] = cecha[i]
    dolny = mediana(array1)
    gorny = mediana(array2)
    return (dolny, gorny)

def odchylenie_standardowe(*cecha):
    srednia = srednia_arytmetyczna(cecha)
    licznik = 0
    for i in range(size):
        licznik += ((cecha[i] - srednia) * (cecha[i] - srednia))
    return math.sqrt(licznik/(size - 1))


print(srednia_arytmetyczna(sepalLenght))
