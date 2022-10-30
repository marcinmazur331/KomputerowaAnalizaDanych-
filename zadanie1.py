from itertools import count
from typing import Counter
import numpy as np

sepalLenght = []
sepalWidth = []
petalLength = []
petalWidth = []
species = []

with open('data.csv', 'r') as file:
    for line in file:
        container = line.split(',')
        sepalLenght.append(float(container[0]))
        sepalWidth.append(float(container[1]))
        petalLength.append(float(container[2]))
        petalWidth.append(float(container[3]))
        species.append(int(container[4]))
        # if (container[4] == "0\n"):
        #     species.append("setosa")
        # if (container[4] == "1\n"):
        #     species.append("versicolor")
        # if (container[4] == "2\n"):
        #     species.append("virginica")

# def getLiczebnosc():
#     setosa = species.count("setosa")
#     versicolor = species.count("versicolor")
#     virginica = species.count("virginica")
#     return (setosa, versicolor, virginica)

# def procenty():
#     return (round(getLiczebnosc()[0] / 150,
#                   2), round(getLiczebnosc()[1] / 150,
#                             2), round(getLiczebnosc()[2] / 150, 2))

# print(procenty()[0], procenty()[1], procenty()[2])


def gonwo(nuber):
    counter = 0
    for i in species:
        if species[i] ==:
            counter += 1
    return counter


gonwo()