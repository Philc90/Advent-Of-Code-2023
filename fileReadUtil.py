def fileToArray(filename):
    arr = []
    with open(filename) as file:
        for line in file:
            arr.append(line.strip())
    return arr
