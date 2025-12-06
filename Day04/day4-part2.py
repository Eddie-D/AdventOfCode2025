file = open("input.txt")

lines = file.readlines()
matrix = [[x for x in l.rstrip()]for l in lines]
numLines = len(lines)
numCols = len(matrix[0])

overallTotal = 0
cycleTotal = 1
while cycleTotal != 0 :
    def checkAdjacencies(i,j) :
        adj = 0
        for a in range(i - 1, i+2) :
            for b in range(j-1, j+2) :
                if (a >= 0 and b >= 0 and a < numLines and b < numCols and not (a == i and b == j)) :
                    adj += 1 if matrix[a][b] != "." else 0
        if adj < 4 :
            matrix[i][j] = "X"
            return 1
        return 0

    cycleTotal = 0
    for i in range(numLines) :
        for j in range (numCols) :
            if matrix[i][j] != "." :
                cycleTotal += checkAdjacencies(i,j)

    for i in range(numLines) :
        for j in range (numCols) :
            if matrix[i][j] == "X" : matrix[i][j] = "."

    overallTotal += cycleTotal

print(f"Total adjacencies {overallTotal}")