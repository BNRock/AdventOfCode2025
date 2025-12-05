file = open("input.txt")
sum = 0
switch = 0
fresh = []
checks = []
for line in (file.read().split("\n")):
    
    if line == "": 
        switch = 1
        continue
    if not switch:
        ranges = line.split("-")
        #print("RANGE: ", ranges)
        fresh.append((int(ranges[0]), int(ranges[1])))
    else:
        checks.append(int(line))
        

for check in checks:
    for r in fresh:
        #print("R1: :", r[0], " R2 ", r[1])
        if check >= r[0] and check <= r[1]:
            #print("PASSED: ", check, " ", r[0], " ", r[1])
            sum += 1
            break
        
#print(fresh)
#print(checks)
print(sum)