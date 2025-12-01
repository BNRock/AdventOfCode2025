file = open("input.txt")
dir = ""
currNum = 50
turnNum = 0
sum = 0
zeroSum = 0
prevNum = 50

for line in (file.read().split("\n")):
    dir = line[0]
    turnNum = int(line[1:])
    sum += turnNum // 100
    turnNum %= 100
    
    if(dir == "L"):
        currNum -= turnNum
    else:
        currNum += turnNum
    
    if (currNum < 0):
        currNum += 100
        if prevNum != 0 and currNum != 0: 
            sum += 1
    elif (currNum > 99):
        currNum -= 100
        if prevNum != 0 and currNum!= 0: 
            sum += 1
        
    if (currNum == 0):
        sum += 1
        
    prevNum = currNum
    
    
print(sum)
