file = open("input.txt")
data = file.read().split(",")
sum = 0

for idRange in data:
    rangeBounds = idRange.split("-")
    idList = list(range(int(rangeBounds[0]), int(rangeBounds[1])+1))
    
    for id in idList:
        idStr = str(id)
        key = len(idStr)//2        
        
        for i in range(key):
            sub = idStr[:i+1]
            subList = []
            
            for j in range(0, len(idStr), i+1):
                subList.append(idStr[j:j+i+1])

            if(len(set(subList)) <= 1):
                sum += id
                break
            

print(sum)
            
