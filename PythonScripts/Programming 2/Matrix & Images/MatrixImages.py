def createMatrix(row: int, column: int, init = 0) -> list[list]:
    M = []
    for _ in range(row):
        row = [init for _ in range(column)]
        M.append(row)
    return M

def printMatrix(M: list[list]):
    s = "{:4}" * getDimension(M)[1]
    for row in M:
        print(s.format(*row))

def getDimension(M: list[list]):
    return len(M), len(M[0]) if M else "Matrix empty."

def alter(M: list[list], row: int, column: int, value: int) -> list[list]:
    M[row][column] = value 
    return M

def drawHorizontalLine(M: list[list], row: int, color: any) -> list[list]:
    M[row] = [color] * getDimension(M)[1]
    return M

def drawVerticalLine(M: list[list], column: int, color: any) -> list[list]:
    for i in range(getDimension(M)[0]):
        M[i][column] = color
    return M


if __name__ == "__main__":
    M = createMatrix(100,100,7)
    printMatrix(M)