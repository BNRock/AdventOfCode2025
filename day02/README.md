- parse line into list
- for loop for each entry:
    - create secondary list for each entry, of numbers contained in range of numbers separated by -
    - for each number, convert to str. if contains even amount of digits, split down middle. if two halves are equal, its invalid and add to sum.

## part 2
- remove even number of digits 
- divide length of number by half. so if number is 8 digits long, key is 4
- for len in key:
    - take first len digits as sample, substring out from number. for len-key times, check if first len digits are the same as sample
    