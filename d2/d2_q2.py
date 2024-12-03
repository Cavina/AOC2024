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
1. Iterate over list
2. Check if list has an item to be removed to make it safe if we find an unsafe report
    - A report is unsafe if:
        (It falls out of bounds and the next item is not breaking montonicity) and we have already cleared one report as safe.

3. If it is safe, we count it.

Check if list has item to be removed

1. Set increasing, decreasing -> T,T
2. set unsafe_to_safe = 0
3. Iterate over list
    Case:
    if arr[i-1] > arr[i]:
        increasing -> False
    if arr[i-1] < arr[i]:
        decreasing -> False 
    -- This determinse if a report is unsafe
    if ((out_of_bounds and not (increasing == decreasing)) and unsafe_to_safe == 1):
        break
    
        
        
'''
lines = input_text.splitlines()
data = [[int(x) for x in line.split()] for line in lines]

safe_count = 0

def is_safe(report):
    increasing = all(1 <= report[i] - report[i-1] <= 3 for i in range(1, len(report)))
    decreasing = all(1 <= report[i-1] - report[i] <= 3 for i in range(1, len(report)))
    return increasing or decreasing

for row in data:
    if is_safe(row):
        safe_count += 1
    else:
        # Try removing one level at a time and check if the report becomes safe
        for i in range(len(row)):
            modified_row = row[:i] + row[i+1:]
            if is_safe(modified_row):
                safe_count += 1
                break  # No need to check further once we find a valid solution

print(safe_count)
