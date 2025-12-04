file = open("input.txt")
sum = 0
remList = []

rows = [line for line in (file.read().split("\n"))]

def removePaper(rows, remList):
    for rem in remList:
        i = rem[0]
        j = rem[1]
        rows[i] = rows[i][:j] + "x" + rows[i][j+1:]
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
    removeList = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            try:
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
                    if adjSum < 4:
                        sum +=1
                        #rows[i] = rows[i][:j] + "!" + rows[i][j+1:]
                        removeList.append((i,j))
                    #print("SUM ", adjSum)
            except IndexError:
                pass
    return sum, removeList

retVal = 1
while retVal > 0:
    retVal, remList = checkAdjacent(rows)
    sum += retVal
    removePaper(rows, remList)

print(sum)
    