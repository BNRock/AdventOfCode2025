- dial starts at 50
- dial goes from 0 to 99, L for lower numbers, R for higher numbers
- sum how many times the dial ends up pointed at 0

## soln
- var for current Number
- var for dir
- var for turn number
- if first letter is L:
    - current number = current number - turnNumber
    - if current number is negative, current number = 100+currentNum
    - if current number is above 99, current number = currentNum-100
    - e.g. 95 R10, currNum is 105, so 105-100 =5, and 5 L10, currNum is -5 so 100+-5 = 95

## part 2
 - everytime number is above 99 or below 0, count that
 - before modding number, int divide by 100, then add to sum