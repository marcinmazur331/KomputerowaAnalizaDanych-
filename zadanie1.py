import numpy as np
import math


sepalLengthTemp = []
sepalWidthTemp = []
petalLengthTemp = []
petalWidthTemp = []
species = []

with open('data.csv', 'r') as file:
    size = 0
    for line in file:
        size += 1
        container = line.split(',')
        sepalLengthTemp.append(float(container[0]))
        sepalWidthTemp.append(float(container[1]))
        petalLengthTemp.append(float(container[2]))
        petalWidthTemp.append(float(container[3]))
        species.append(int(container[4]))


def bubbleSort(arr):
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


sepalLength = np.array([sepalLengthTemp])
sepalWidth = np.array([sepalWidthTemp])
petalLength = np.array([petalLengthTemp])
petalWidth = np.array([petalWidthTemp])
bubbleSort(sepalLengthTemp)
bubbleSort(sepalWidthTemp)
bubbleSort(petalLengthTemp)
bubbleSort(petalWidthTemp)

def liczebnosc(number):
    counter = 0
    for i in range(size):
        if species[i] == number:
            counter += 1
    return counter


def udzial_procentowy(nazwa):
    return round((liczebnosc(nazwa) / size) * 100, 1)


def maksimum(cecha):
    max = -1
    for i in range(size):
        if cecha[0][i] > max:
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


def mediana(cecha): # uzywac tempa
    index = math.floor(size / 2) - 1
    if size % 2 == 0:
        return round((cecha[index] + cecha[index + 1]) / 2, 2)
    return cecha[int(size / 2) + 1]


def kwartyl(cecha): # uzywac tempa
    firstQuadIndex = math.floor(size / 4) - 1
    thirdQuadIndex = math.ceil(size * 3 / 4) - 1
    if (math.floor(size / 2) % 2 == 0):
        return ((cecha[firstQuadIndex] + cecha[firstQuadIndex + 1]) / 2,
                (cecha[thirdQuadIndex] + cecha[thirdQuadIndex + 1]) / 2)
    return (cecha[firstQuadIndex + 1], cecha[thirdQuadIndex])


def odchylenie_standardowe(cecha):
    srednia = srednia_arytmetyczna(cecha)
    licznik = 0
    for i in range(size):
        licznik += ((cecha[0][i] - srednia) * (cecha[0][i] - srednia))
    return math.sqrt(licznik / (size - 1))


print("srednia", srednia_arytmetyczna(sepalLength))
print("kwartyl dolny i gorny", kwartyl(sepalLengthTemp))
print("odchylenie", odchylenie_standardowe(sepalLength))
print("liczebnosc",liczebnosc(0))
print("udzial procentowy", udzial_procentowy(0))
print("minimum", minimum(sepalLength))
print("maksimum", maksimum(sepalLength))
print("mediana", mediana(sepalLengthTemp))