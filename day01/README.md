- dial starts at 50
- dial goes from 0 to 99, L for lower numbers, R for higher numbers
- sum how many times the dial ends up pointed at 0

## soln
- var for current Number
- var for dir
- var for turn number
- if first letter is L:
    - current number = current number - turnNumber
    - if current number is negative, current number = 100-turnNum
    - if current number is above 99, current number = turnNum - 100