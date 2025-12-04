- input is line of numbers, goal is to select 2 numbers in sequence to make the largest posible number, then sum them all

## soln
- create dictionary where keys are the digits, and the values are lists with their positions. sort dictionary. then for each key-position (starting from lowest position in highest key), see if there exists another key with a greater position. If so, this must be the highest number since I'm sorting descending. Combine the two keys and add to sum

- wow okay that was stupid. turns out you can just compare the two digits as you read the number left to right. take the first 2 digits as the largest number. then take the rest of the number dig by dig. if digit is bigger than num1, replace num1 with it, and num2 with the number after. If its not bigger than num1, then is it bigger than num2? if so, replace num2 with it. continue to the end of the line.

## part 2
- same concept as part 1. just building a number sequentially. if number is bigger than num1, replace it and take the next 11 digits as the rest. otherwise