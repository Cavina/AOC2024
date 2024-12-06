from setup.get_input import fetch_aoc_input
import re
try:
    input_text = fetch_aoc_input(5)
except Exception as e:
    print(e)




'''
X|Y
Page X must be printed before Y
n1,n2,n3,n4,n5
is an update. We want it to be in the right order
s.t. there is no rule n2|n1 or we can say that it must be true that
n1 will always come before n2

Set the rules
1. We can create a map with X as key, and an array of values that come after the key.  O(n)
Identify updates that are in the right order.

Given a list A
A is in the right order if for every number in A, that  A[i-1]|A[i..n] or A[i..n] must come after
A[i-1]. This translates to A[i..n] being in the value array for A[i-1] (This should include all the previous rules.) or has no rule set 

If it's in the array or not in the array, then it is a safe page placement

Brute force single list:
hash_map -> populated
safe = True
for i -> 1 to len(arr):
    for j -> i+1 to len(arr)-1:
        key = arr[i]
        if hash_map[key] and not arr[j] in hash_map[key]:
            return False
            
            
if safe:
    score += getMiddleNumber(arr)

            
            
            
            



'''
# print(input_text.splitlines())
'''
split this list where the value is ''
I need to extract the numbers from 
page_rules and put them in a list

'''
input_text = input_text.splitlines()
separator = input_text.index('')
page_rules_strings = input_text[:separator]
page_updates_strings = input_text[separator+1:]
pattern = re.compile(r'(\d+)\|(\d+)')

'''
Create a hash_map to store the numbers
Iterate over page_rules_strings.
For each string I will extract the two numbers
and I will check if n1 is in the hash_map.
If not, I will add it to the hash_map and add [n2] 
as the value
if it is in the map, I just append n2 to the value list

page_rules = {}
for s in page_rules_strings:
    match = pattern.match(s)
    if match:
        n1, n2 = match.groups()
        if n1 in page_rules:
            pages_rules[n1] = page_rules[n1].append(n2)
        else:
            pages_rules[n1] = [n2]


'''
page_rules = {}
page_updates = [list(map(int, s.split(','))) for s in page_updates_strings]


for s in page_rules_strings:
    match = pattern.match(s)
    if match:
        n1, n2 = match.groups()
        n1, n2 = int(n1), int(n2)
        if n1 in page_rules:
            page_rules[n1].append(n2)
        else:
            page_rules[n1] = [n2]



score = 0
def is_safe_update(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)-1):
            key = update[i]
            if key in page_rules and not (update[j] in page_rules[key]):
                return False
    return True


for test in page_updates:
    if is_safe_update(test):
        #THis might need to account for odd/even
        score +=  test[len(test)//2]   

print(score)