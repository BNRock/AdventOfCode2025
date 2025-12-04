file = open("input.txt")
sum = 0

rows = [line for line in (file.read().split("\n"))]

def checkNonNeg(rows, i, j):
    try:
        if i >= 0 and j >= 0:
            if rows[i][j] == "@":
                return True
        return False
    except IndexError:
        pass
    
def checkAdjacent(rows):
    sum = 0
    
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if(rows[i][j] == "@"):
                #print("ROW ", i, "COL ", j)
                adjSum = 0
                if(checkNonNeg(rows, i, j-1)): adjSum +=1
                if(checkNonNeg(rows, i, j+1)): adjSum +=1
                if(checkNonNeg(rows, i-1, j-1)): adjSum +=1
                if(checkNonNeg(rows, i-1, j)): adjSum +=1
                if(checkNonNeg(rows, i-1, j+1)): adjSum +=1
                if(checkNonNeg(rows, i+1, j-1)): adjSum +=1
                if(checkNonNeg(rows, i+1, j)): adjSum +=1
                if(checkNonNeg(rows, i+1, j+1)): adjSum +=1
                if adjSum < 4: sum +=1
                #print("SUM ", adjSum)
    return sum

print(checkAdjacent(rows))

    
    