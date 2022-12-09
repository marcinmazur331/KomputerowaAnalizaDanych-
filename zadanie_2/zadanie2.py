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
