def kwartyl(cecha):
    array1 = np.array(int(size / 2))
    array2 = np.array(int(size / 2))
    if size % 2 == 0:
        for i in range(int(size / 2)):
            np.append(array1, cecha[0][i])
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