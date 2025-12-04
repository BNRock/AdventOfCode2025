file = open("input.txt")
sum = 0
isBreak = False

def findMax(sd):
    
    sum = 0
    for key in sd:
        for i in sd.get(key):
            for key1 in sd:
                if any(x > i for x in sd.get(key1)):
                    print("NUM: ", key, key1)
                    sum += int(key + key1)
                    print("SUM ", sum)
                    return sum
                                
for line in (file.read().split("\n")):
    max = int(line[0])
    max1Pos = 0
    d = {}
    for pos, dig in enumerate(line):
        if(dig in d):
            d.get(dig).append(pos)
        else:
            tempList = [pos]
            d[dig] = tempList
            tempList = []
    
    keys = list(d.keys())
    keys.sort(reverse=True)
    
    sd = {i: d[i] for i in keys}
    
    print("LINE: ", line)
    print("SD: ",sd)
    sum += findMax(sd)
    
    print("FINAL SUM: ", sum)