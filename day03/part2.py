file = open("input.txt")
sum = 0               
added = 0

def findMaxNum(line):
    retNum = ""
    numList = [line.pop(0)]
    for i in range(len(line)):
        added = 0
        dig = line.pop(0)
        if(len(line) < 12):
            startIdx = 12-len(line)-1
        else:
            startIdx = 0
        for i in range(startIdx, len(numList)):
            if dig > numList[i]:
                numList[i] = dig
                del numList[i+1:]
                added = 1
                break
        if len(numList) < 12 and not added:
            numList.append(dig)
    
    for num in numList:
        retNum += num
    
    return int(retNum)
                                 
for line in (file.read().split("\n")):
    lineList = [dig for dig in line]
    sum += findMaxNum(lineList)
    
print(sum)