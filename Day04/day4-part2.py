file = open("input.txt")

lines = file.readlines()
matrix = [[x for x in l.rstrip()]for l in lines]
numLines = len(lines)
numCols = len(matrix[0])
print(f"nl: {numLines}")
print(f"nc: {numCols}")
print(f"matrix: {matrix}")

def checkAdjacencies(i,j) :
    total = 0
    for a in range(i - 1, i+2) :
        for b in range(j-1, j+2) :
            if (a >= 0 and b >= 0 and a < numLines and b < numCols and not (a == i and b == j)) :
                total += 1 if matrix[a][b] != "." else 0
    return 1 if total < 4 else 0

total = 0
for i in range(numLines) :
    for j in range (numCols) :
        if (matrix[i][j] != ".") :
            total += checkAdjacencies(i,j)

print(f"Total adjacencies {total}")