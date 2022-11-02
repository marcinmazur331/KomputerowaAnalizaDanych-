# Autorzy: Piotr Płeska 242499      Marcin Mazur 242467

import numpy as np
import math
from matplotlib import pyplot as plt

sepalLengthTemp = []
sepalWidthTemp = []
petalLengthTemp = []
petalWidthTemp = []
species = []

setosaSepalLength = []
versicolorSepalLength = []
virginicaSepalLength = []

setosaSepalWidth = []
versicolorSepalWidth = []
virginicaSepalWidth = []

setosaPetalLength = []
versicolorPetalLength = []
virginicaPetalLength = []

setosaPetalWidth = []
versicolorPetalWidth = []
virginicaPetalWidth = []

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
        if container[4] == '0\n':
            setosaSepalLength.append(float(container[0]))
            setosaSepalWidth.append(float(container[1]))
            setosaPetalLength.append(float(container[2]))
            setosaPetalWidth.append(float(container[3]))
        if container[4] == '1\n':
            versicolorSepalLength.append(float(container[0]))
            versicolorSepalWidth.append(float(container[1]))
            versicolorPetalLength.append(float(container[2]))
            versicolorPetalWidth.append(float(container[3]))
        if container[4] == '2\n':
            virginicaSepalLength.append(float(container[0]))
            virginicaSepalWidth.append(float(container[1]))
            virginicaPetalLength.append(float(container[2]))
            virginicaPetalWidth.append(float(container[3]))


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
    return round(max, 2)


def minimum(cecha):
    min = 1000
    for i in range(size):
        if cecha[0][i] < min:
            min = cecha[0][i]
    return round(min, 2)


def srednia_arytmetyczna(cecha):
    suma = 0.0
    for i in range(size):
        suma = suma + cecha[0][i]
    return round(suma / size, 2)


def mediana(cecha):
    index = math.floor(size / 2) - 1
    if size % 2 == 0:
        return round((cecha[index] + cecha[index + 1]) / 2, 2)
    return round(cecha[int(size / 2) + 1], 2)


def kwartyl(cecha):
    firstQuadIndex = math.floor(size / 4) - 1
    thirdQuadIndex = math.ceil(size * 3 / 4) - 1
    if math.floor(size / 2) % 2 == 0:
        return (round((cecha[firstQuadIndex] + cecha[firstQuadIndex + 1]) / 2, 2),
                (round(cecha[thirdQuadIndex] + cecha[thirdQuadIndex + 1]) / 2), 2)
    return round(cecha[firstQuadIndex + 1], 2), round(cecha[thirdQuadIndex], 2)


def odchylenie_standardowe(cecha):
    srednia = srednia_arytmetyczna(cecha)
    licznik = 0
    for i in range(size):
        licznik += ((cecha[0][i] - srednia) * (cecha[0][i] - srednia))
    return round(math.sqrt(licznik / (size - 1)), 2)


def histogram(cecha, tytul, string, bins, max):
    plt.subplots(figsize=(10, 7))
    plt.hist(cecha, bins=bins, edgecolor='black', linewidth=3)
    plt.title(tytul, fontsize=25)
    plt.ylabel('Liczebność', fontsize=20)
    plt.xlabel(string, fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(range(0, max, 5))
    plt.show()


def pudelkowy(setosaCecha, versicolorCecha, virginicaCecha, string):
    plt.figure(figsize=(10, 7))
    plt.xlabel('Gatunek', fontsize=20)
    plt.ylabel(string, fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    caps = dict(linewidth=3)
    whiskers = dict(linewidth=3)
    fliers = dict(markersize=12, linewidth=9, markeredgewidth=3)
    boxes = dict(linewidth=3)
    medians = dict(linewidth=3)
    plt.boxplot([setosaCecha, versicolorCecha, virginicaCecha],
                labels=['setosa', 'versicolor', 'virginica'], capprops=caps,
                whiskerprops=whiskers, flierprops=fliers, boxprops=boxes, medianprops=medians)
    plt.show()


# print("Liczebnosc setosa: ",liczebnosc(0))
# print("Udzial procentowy setosa:", udzial_procentowy(0))
# print("Liczebnosc versicolor: ",liczebnosc(1))
# print("Udzial procentowy versicolor: ", udzial_procentowy(1))
# print("Liczebnosc virginica: ",liczebnosc(2))
# print("Udzial procentowy virginica: ", udzial_procentowy(2))

# print("Minimum Długości działki kielicha (cm): ", minimum(sepalLength))
# print("Minimum Szerokości działki kielicha (cm): ", minimum(sepalWidth))
# print("Minimum Długości płatka (cm): ", minimum(petalLength))
# print("Minimum Szerokości płatka (cm): ", minimum(petalWidth))

# print("Srednia Długość działki kielicha (cm): ", srednia_arytmetyczna(sepalLength))
# print("Odchylenie Długości działki kielicha (cm): ", odchylenie_standardowe(sepalLength))
# print("Srednia Szerokość działki kielicha (cm): ", srednia_arytmetyczna(sepalWidth))
# print("Odchylenie Szerokości działki kielicha (cm): ", odchylenie_standardowe(sepalWidth))
# print("Srednia Długość płatka (cm): ", srednia_arytmetyczna(petalLength))
# print("Odchylenie Długości płatka (cm): ", odchylenie_standardowe(petalLength))
# print("Srednia Szerokość płatka (cm): ", srednia_arytmetyczna(petalWidth))
# print("Odchylenie Szerokości płatka (cm): ", odchylenie_standardowe(petalWidth))

# print("Mediana Długości działki kielicha (cm): ", mediana(sepalLengthTemp))
# print("Kwartyl dolny i gorny Długości działki kielicha (cm): ", kwartyl(sepalLengthTemp))
# print("Mediana Szerokości działki kielicha (cm): ", mediana(sepalWidthTemp))
# print("Kwartyl dolny i gorny Szerokości działki kielicha (cm): ", kwartyl(sepalWidthTemp))
# print("Mediana Długości płatka (cm): ", mediana(petalLengthTemp))
# print("Kwartyl dolny i gorny Długości płatka (cm): ", kwartyl(petalLengthTemp))
# print("Mediana  Szerokości płatka (cm): ", mediana(petalWidthTemp))
# print("Kwartyl dolny i gorny  Szerokości płatka (cm): ", kwartyl(petalWidthTemp))

# print("Maksimum Długości działki kielicha (cm): ", maksimum(sepalLength))
# print("Maksimum Szerokości działki kielicha (cm): ", maksimum(sepalWidth))
# print("Maksimum Długości płatka (cm): ", maksimum(petalLength))
# print("Maksimum Szerokości płatka (cm): ", maksimum(petalWidth))


bin1 = [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
bin2 = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
bin3 = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
bin4 = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
max1 = 40
max2 = 75
max3 = 30
max4 = 50

# histogram(sepalLength[0], 'Długość działki kielicha', 'Długość (cm)', bin1, max1)
# histogram(sepalWidth[0], 'Szerokość działki kielicha', 'Szerokość (cm)', bin2, max2)
# histogram(petalLength[0], 'Długość płatka', 'Długość (cm)', bin3, max3)
# histogram(petalWidth[0], 'Szerokość płatka', 'Szerokość (cm)', bin4, max4)
# pudelkowy(setosaSepalLength, versicolorSepalLength, virginicaSepalLength, 'Długość (cm)')
# pudelkowy(setosaSepalWidth, versicolorSepalWidth, virginicaSepalWidth, 'Szerokość (cm)')
# pudelkowy(setosaPetalLength, versicolorPetalLength, virginicaPetalLength, 'Długość (cm)')
# pudelkowy(setosaPetalWidth, versicolorPetalWidth, virginicaPetalWidth, 'Szerokość (cm)')
