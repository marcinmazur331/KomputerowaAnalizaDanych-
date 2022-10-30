import numpy as np
import math

sepalLenghtTemp = []
sepalWidthTemp = []
petalLengthTemp = []
petalWidthTemp = []
species = []

with open('test.csv', 'r') as file:
    size = 0
    for line in file:
        size += 1
        container = line.split(',')
        sepalLenghtTemp.append(float(container[0]))
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
                arr[0][j + 1] = temp


sepalLenght = np.array([sepalLenghtTemp])
sepalWidth = np.array([sepalWidthTemp])
petalLength = np.array([petalLengthTemp])
petalWidth = np.array([petalWidthTemp])


def liczebnosc(number):
    counter = 0
    for i in range(size):
        if species[i] == number:
            counter += 1
    return counter


def udzial_procentowy(nazwa):
    return round(liczebnosc(nazwa) / size, 2)


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


def mediana(cecha):
    # sortowanie
    index = math.floor(size / 2) - 1
    if size % 2 == 0:
        return round((cecha[0][index] + cecha[0][index + 1]) / 2, 2)
    return cecha[0][int(size / 2) + 1]


# def kwartyl(cecha):
#     array1 = np.array(int(size / 2))
#     array2 = np.array(int(size / 2))
#     if size % 2 == 0:
#         for i in range(int(size / 2)):
#             np.append(array1, cecha[0][i])
#         for i in range(int(size / 2) + 1, size):
#             np.append(array1, cecha[0][i])
#         dolny = mediana(array1[0])
#         gorny = mediana(array2[0])
#         return (dolny, gorny)
#     for i in reversed(range(int(size / 2))):
#         array1[i] = cecha[0][i]
#     for i in range(math.floor(size / 2) + 1, size):
#         array2[i] = cecha[0][i]
#     dolny = mediana(array1)
#     gorny = mediana(array2)
#     return (dolny, gorny)


def kwartyl(cecha):
    # sortowanie
    firstQuadIndex = math.floor(size / 4) - 1
    thirdQuadIndex = math.ceil(size * 3 / 4) - 1
    if (math.floor(size / 2) % 2 == 0):
        return ((cecha[0][firstQuadIndex] + cecha[0][firstQuadIndex + 1]) / 2,
                (cecha[0][thirdQuadIndex] + cecha[0][thirdQuadIndex + 1]) / 2)
    return (cecha[0][firstQuadIndex + 1], cecha[0][thirdQuadIndex])


def odchylenie_standardowe(cecha):
    srednia = srednia_arytmetyczna(cecha)
    licznik = 0
    for i in range(size):
        licznik += ((cecha[0][i] - srednia) * (cecha[0][i] - srednia))
    return math.sqrt(licznik / (size - 1))


# print(srednia_arytmetyczna(sepalLenght))
print(kwartyl(sepalWidth))
# print(odchylenie_standardowe(petalLength))
# print(liczebnosc(2))
# print(udzial_procentowy(0))
# print(minimum(sepalLenght))
# print(maksimum(sepalLenght))
# print(mediana(petalWidth))
