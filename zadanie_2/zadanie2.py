# Autorzy: Piotr Płeska 242499      Marcin Mazur 242467

import numpy as np
from matplotlib import pyplot as plt

sepalLength = []
sepalWidth = []
petalLength = []
petalWidth = []

with open('data.csv', 'r') as file:
    size = 0
    for line in file:
        size += 1
        container = line.split(',')
        sepalLength.append(float(container[0]))
        sepalWidth.append(float(container[1]))
        petalLength.append(float(container[2]))
        petalWidth.append(float(container[3]))



def scatterPlot(cechax, cechay, wspolczynnikPearsona, stringx, stringy, minx, maxx, skokx, miny, maxy, skoky):
    plt.subplots(figsize=(10, 7))
    plt.scatter(cechax, cechay, s=300)
    plt.xlabel(stringx, fontsize=20)
    plt.ylabel(stringy, fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.xticks(np.arange(minx, maxx, step=skokx))
    plt.yticks(np.arange(miny, maxy, step=skoky))
    a, b = np.polyfit(cechax, cechay, deg=1)
    plt.axline(xy1=(0, b), slope=a, color='r', linewidth=3)
    plt.xlim(xmin=minx-0.2, xmax=maxx-skokx+0.2)
    plt.ylim(ymin=miny-0.2, ymax=maxy-skoky+0.2)
    plt.title(f'r = {round(wspolczynnikPearsona, 2)}; y = {a:.1f}x {b:+.1f}', fontsize=20)
    plt.show()


wspolczynnikPearsona1 = np.corrcoef(sepalLength, sepalWidth)[0][1]
wspolczynnikPearsona2 = np.corrcoef(sepalLength, petalLength)[0][1]
wspolczynnikPearsona3 = np.corrcoef(sepalLength, petalWidth)[0][1]
wspolczynnikPearsona4 = np.corrcoef(sepalWidth, petalLength)[0][1]
wspolczynnikPearsona5 = np.corrcoef(sepalWidth, petalWidth)[0][1]
wspolczynnikPearsona6 = np.corrcoef(petalLength, petalWidth)[0][1]


# scatterPlot(sepalLength, sepalWidth, wspolczynnikPearsona1, 'Długość działki kielicha (cm)', 'Szerekość działki kielicha (cm)', 4, 9, 1, 2, 5, 0.5)
# scatterPlot(sepalLength, petalLength, wspolczynnikPearsona2, 'Długość działki kielicha (cm)', 'Długość płatka (cm)', 4, 9, 1, 1, 9, 1)
# scatterPlot(sepalLength, petalWidth, wspolczynnikPearsona3, 'Długość działki kielicha (cm)', 'Szerekość płatka (cm)', 4, 9, 1, 0, 3.5, 0.5)
# scatterPlot(sepalWidth, petalLength, wspolczynnikPearsona4, 'Szerokość działki kielicha (cm)', 'Długość płatka (cm)', 2, 5, 0.5, 1, 8, 1)
# scatterPlot(sepalWidth, petalWidth, wspolczynnikPearsona5, 'Szerekość działki kielicha (cm)', 'Szerokość płatka (cm)', 2, 5, 0.5, 0, 3, 0.5)
# scatterPlot(petalLength, petalWidth, wspolczynnikPearsona6, 'Długość płatka (cm)', 'Szerokość płatka (cm)', 1, 8, 1, 0, 3, 0.5)


