file = open("input.txt")
sum = 0
switch = 0
fresh = []
checks = []
for line in (file.read().split("\n")):
    
    if line == "": 
        break
    
    ranges = line.split("-")
    #print("RANGE: ", ranges)
    fresh.append((int(ranges[0]), int(ranges[1])))

fresh.sort()

merged = []
start, end = fresh[0]

for s,e in fresh[1:]:
    if s <= end:
        end = max(end, e)
    else:
        merged.append((start,end))
        start,end = s,e
        
        
merged.append((start, end))

for s,e in merged:
    sum += (e-s+1)

print(sum)