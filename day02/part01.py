file = open("input.txt")
data = file.read().split(",")
sum = 0

for idRange in data:
    rangeBounds = idRange.split("-")
    idList = list(range(int(rangeBounds[0]), int(rangeBounds[1])+1))
    
    for id in idList:
        idStr = str(id)
        if (len(idStr) % 2 == 0): #If ID is even amount of digits
            id1 = idStr[:len(idStr)//2]
            id2 = idStr[len(idStr)//2:]

            if (id1 == id2):
                sum += int(idStr)

print(sum)
            
