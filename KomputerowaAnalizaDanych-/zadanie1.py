import numpy as np
import math

sepalLenghtTemp = []
sepalWidthTemp = []
petalLengthTemp = []
petalWidthTemp = []
speciesTemp = []
with open('test.csv', 'r') as file:
    size = 0
    for line in file:
        size += 1
        container = line.split(',')
        sepalLenghtTemp.append(float(container[0]))
        sepalWidthTemp.append(float(container[1]))
        petalLengthTemp.append(float(container[2]))
        petalWidthTemp.append(float(container[3]))
        if container[4] == "0\n":
            speciesTemp.append("setosa")
        if container[4] == "1\n":
            speciesTemp.append("versicolor")
        if container[4] == "2\n":
            speciesTemp.append("virginica")


def bubbleSort(arr):
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[0][j + 1] = temp


bubbleSort(sepalLenghtTemp)
bubbleSort()

sepalLenght = np.array([sepalLenghtTemp])
sepalWidth = np.array([sepalWidthTemp])
petalLength = np.array([petalLengthTemp])
petalWidth = np.array([petalWidthTemp])
species = np.array([speciesTemp])


def liczebnosc(nazwa):
    counter = 0
    for i in species:
        if species[i] == nazwa:
            counter += 1
    return counter


def udzial_procentowy(nazwa):
    return round(liczebnosc(nazwa) / size, 2)


def maksimum(cecha):
    max = -1
    for i in range(size):
        if cecha[i] > max:
            max = cecha[0][i]
    return max


def minimum(cecha):
    min = 1000
    for i in range(size):
        if cecha[0][i] < min:
            min = cecha[0][i]
    return min


def srednia_arytmetyczna(cecha):
    suma = 0.0
    for i in range(size):
        suma = suma + cecha[0][i]
    return suma / size


def mediana(cecha):
    bubbleSort(cecha[0].astype(list))
    if size % 2 == 0:
        return round(
            (cecha[0][int(size / 2)] + cecha[0][(int(size / 2)) + 1]) / 2, 2)
    return cecha[0][int(size / 2) + 1]


def kwartyl(cecha):
    bubbleSort(cecha[0][0])
    array1 = np.empty(int(size / 2))
    array2 = np.empty(int(size / 2))
    if size % 2 == 0:
        for i in range(int(size / 2)):
            array1.fill(cecha[0][i])
        for i in range(int(size / 2) + 1, size):
            array2.fill(cecha[0][i])
        dolny = mediana(array1)
        gorny = mediana(array2)
        return (dolny, gorny)
    for i in reversed(range(int(size / 2))):
        array1[i] = cecha[0][i]
    for i in range(math.floor(size / 2) + 1, size):
        array2[i] = cecha[0][i]
    dolny = mediana(array1)
    gorny = mediana(array2)
    return (dolny, gorny)


def odchylenie_standardowe(cecha):
    srednia = srednia_arytmetyczna(cecha)
    licznik = 0
    for i in range(size):
        licznik += ((cecha[0][i] - srednia) * (cecha[0][i] - srednia))
    return math.sqrt(licznik / (size - 1))


# print(srednia_arytmetyczna(sepalLenght))
print(kwartyl(sepalWidth)[0])
# print(odchylenie_standardowe(petalLength))
# print(mediana(petalWidthTemp))
