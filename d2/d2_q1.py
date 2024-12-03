from get_input import fetch_aoc_input

try:
    input_text = fetch_aoc_input(2)
except Exception as e:
    print(e)


'''
A report is a row
A level is an element in a row

I need stricly increasing or decreasing for list 1
If the difference between the i-1th and i+1th is greater than one
and less than three, it is safe

How many reports are safe?

Brute force for a single list
1. Check if the list is strictly increasing or strictly decreasing.
    If its false, we return false
2. Check that 1 <= abs(row[i]-row[i+1]) <=3
    If false, return false.
   OTherwise, return true

Checking if list is monotic:
Increasing
1. row[i-1] < row[i] < row[i+1] and i > 0

Decreasing
Case: 
1. row[i-1] >row[i] > row[i+1] and i > 0

Monotonic:
increasing -> True
decreasing -> True

for i -> 0 to len(range(row)):
    if i > 0 and row[i-1] < row[i]:
        decreasing -> False
    if i > 0 and row[i-1] > row[i]:
        increasing -> False
    
    if i > 0 and not (1 <= abs(row[i]-row[i-1] <= 3):
        return False

    return increasing or decreasing

 
'''

lines = input_text.splitlines()
data = []
for line in lines:
    numbers = [int(x) for x in line.split()]
    data.append(numbers)

safe = 0

for row in data:
    decreasing, increasing = True, True
    for i in range(len(row)):
        if i > 0:
            if row[i-1] < row[i]:
                decreasing = False
            if row[i-1] > row[i]:
                increasing = False
            if not (1 <= abs(row[i]-row[i-1]) <= 3):
                increasing = decreasing = False
                break

    if increasing or decreasing:
        safe += 1

print(safe) 

