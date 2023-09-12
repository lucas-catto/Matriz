
matriz_00 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

matriz_01 = [
    [9,8,7],
    [6,5,4],
    [3,2,1],
]

# Sum of Matriz
sumMatriz = []

for valueLine in range(len(matriz_00)):
    
    rowSum = []

    for valueColumn in range(len(matriz_01)):
        rowSum.append(matriz_00[valueLine][valueColumn] + matriz_01[valueLine][valueColumn])

    sumMatriz.append(rowSum)


for row in sumMatriz: print(row)

# ----------------------------------------

# Subtraction of Matriz

sumMatriz = []

for valueLine in range(len(matriz_00)):
    
    rowSum = []

    for valueColumn in range(len(matriz_01)):
        rowSum.append(matriz_00[valueLine][valueColumn] - matriz_01[valueLine][valueColumn])

    sumMatriz.append(rowSum)


for row in sumMatriz: print(row)

# ----------------------------------------
