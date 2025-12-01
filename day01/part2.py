file = open("input.txt")
dir = ""
currNum = 50
turnNum = 0
sum = 0

for line in (file.read().split("\n")):
    dir = line[0]
    turnNum = int(line[1:]) % 100
    
    if(dir == "L"):
        currNum -= turnNum
    else:
        currNum += turnNum
    
    if (currNum < 0):
        currNum += 100
    elif (currNum > 99):
        currNum -= 100
    
    if (currNum == 0):
        sum += 1
    
print(sum)
