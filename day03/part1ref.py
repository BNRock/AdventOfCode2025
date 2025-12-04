file = open("input.txt")
sum = 0
                                
for line in (file.read().split("\n")):
    prevMax = line[0]
    num1 = line[0]
    num2 = line[1]
    for pos,num in enumerate(line[2:-1]):
        if(num > num1):
            num1 = num
            num2 = line[pos+3]
        elif(num > num2):
            num2 = num
            
    num2 = line[-1] if line[-1] > num2 else num2
    
    sum += int(str(num1)+str(num2))
    
print(sum)