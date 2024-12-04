from setup.get_input import fetch_aoc_input
import re
try:
    input_text = fetch_aoc_input(3)
except Exception as e:
    print(e)
'''
1. Iterate over string
2. If "mul" not in string continue to next
   Otherwise, strip the string down to the number and parentheses
   and add it to the list

'''



# Extract all valid (num1, num2) pairs as integer tuples
def calculate_mul_instr(pattern, input_str):
    score = 0
    matches = [
        (int(num1), int(num2))  # Convert to tuple of integers
        for num1, num2 in pattern.findall(input_str)  # Find all matches
    ]

    for n in matches:
        score += n[0]*n[1]
        
    return score

pattern = re.compile(r'mul\((\d+),(\d+)\)')
score = calculate_mul_instr(pattern, input_text)
print(score)
'''
1. Get index of dont, from the end of that dont(), we look for the index of do,
    then we pass the substring of the two indices as the input text 
    we store that in the dont_score 
    and we subtract the two: score-dont_score

'''
i = 0
dont_score = 0
while i < len(input_text):
    start_idx = input_text.find("don't()", i)

    if start_idx == -1:
        break

    end_idx = input_text.find("do()", start_idx)

    if end_idx != -1:
        dont_score += calculate_mul_instr(pattern, input_text[start_idx:end_idx])
    
    i = end_idx + 1

print(score-dont_score)