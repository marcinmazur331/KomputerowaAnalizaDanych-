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
        if (container[4] == "0\n"):
            species.append("setosa")
        if (container[4] == "1\n"):
            species.append("versicolor")
        if (container[4] == "2\n"):
            species.append("virginica")

print(
    "No. \t",
    "species\t",
    "sepalLenght\t",
    "sepalWidth\t",
    "petalLength\t",
    "petalWidth\t",
)
for i in range(150):
    print(
        i + 1,
        species[i],
        sepalLenght[i],
        sepalWidth[i],
        petalLength[i],
        petalWidth[i],
    )
