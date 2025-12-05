file = open("input.txt")
sum = 0
switch = 0
appendSet = 0

fresh = []
set1 = set2 = False
for line in (file.read().split("\n")):
    
    if line == "": 
        switch = 1
        break
    if not switch:
        ranges = line.split("-")
        r0 = int(ranges[0])
        r1 = int(ranges[1])
        #print("RANGE: ", ranges)
        
        
        for r in fresh:
            #print("FRESH: ", fresh)
            #print("1: R: ", r,  " LINE: ", line, "SET1 ", set1, " SET2 ", set2)
            
            if r[0] <= r0 <= r[1]:
                set1=True #if new lower range is between existing range
                #print("SET1: ", r0)
            elif r0 < r[0] and r[0] <= r1 <= r[1]:
                if r[0]-r0 < prevmax:
                    prevmax = r[0]-r0
                    closestOver = r[0]
                    #print(" OVER r0: ", r0, " over ", closestOver)
            if r[0] <= r1 <= r[1]:
                set2=True #if new higher range is between existing range
                #print("SET2: ", r1)
            elif set1 and r1 > r[1]:
                if r1-r[1] < prevdif:
                    prevdif = r1-r[1]
                    closestUnder = r[1]
                    #print("r1: ", r1, " Under ", closestUnder)
            if r[0] <= r0 <= r[1] and r[0] <= r1 <= r[1]:
                #print("BREAK")
                break
            if set1 and set2: #set is already including in list
                #print("ADD RANGE: ", closestUnder+1, " ", closestOver-1)
                appendSet = 1
            #set1 = set2 = False
            #print("2: R: ", r,  " LINE: ", line, "SET1 ", set1, " SET2 ", set2)
            
        if not set1 and not set2: 
            fresh.append((r0, r1))
            #print("APPENDED, ", fresh)
        if set1 and not set2: #set lower limit is already included, but upper limit not (eg 12-22 in example input, 12 included but 20-22 not)
            fresh.append((closestUnder+1,r1))
            #print("APPENDED2, ", fresh)
        if set2 and not set1:
            fresh.append((r0, closestOver-1))
            #print("APPENDED3, ", fresh)
        if appendSet:
            fresh.append((closestUnder+1, closestOver-1))
            #print("APPENDED4, ", fresh)
        closestUnder = 0
        closestOver = 0
        appendSet = 0
        prevdif = 9999999999999999999999999999999999999999999
        prevmax = 9999999999999999999999999999999999999999999
        set1 = set2 = False
            
for r in fresh:
    sum += r[1]-r[0]+1
        
#print(fresh)

print(sum)