from setup.get_input import fetch_aoc_input
import re
try:
    input_text = fetch_aoc_input(5)
except Exception as e:
    print(e)



input_text = input_text.splitlines()
separator = input_text.index('')
page_rules_strings = input_text[:separator]
page_updates_strings = input_text[separator+1:]
pattern = re.compile(r'(\d+)\|(\d+)')

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




def is_safe_update(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)-1):
            key = update[i]
            if key in page_rules and not (update[j] in page_rules[key]):
                return False
    return True

def swap_bad_update(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)-1):
            key = update[i]
            if key in page_rules and not (update[j] in page_rules[key]):
                update[i], update[j] = update[j], update[i]
# safe_score = 0
# updated_list_score = 0
# for test in page_updates:
#     if is_safe_update(test):
#         #THis might need to account for odd/even
#         safe_score +=  test[len(test)//2]   
#     else:
#         swap_bad_update(test)
#         #updated_list_score += test[len(test)//2]   

'''
Given a list that's not ordered correclty, A put it in order.
i -> 0
j -> 0
n -> len(list)
while i < n:
    key = update[i]
    if key is in the page_rules and and update[j] is not in the values array, 
        we swap
        increment j
    increment i


'''
# test = [75,97,47,61,53]
# i = 0
# n = len(test)
# update = test
# while i < n - 1:
#     key = update[i]
#     j = i+1
#     if key in page_rules and update[j] not in page_rules[key]:
#         update[i], update[j] = update[j], update[i]
#     else:
#         i += 1  
# #swap_bad_update(update)
# print(update)

test = [97, 13, 75, 29, 47]
i = 0
def reorder_update(update, page_rules):
    # Initialize flag to track if any swaps were made
    ordered = False
    
    # We will repeatedly loop through the update until no more violations are found
    while not ordered:
        ordered = True  # Assume the update is correctly ordered unless proven otherwise
        
        # Try to detect violations by comparing every pair of pages
        for i in range(len(update) - 1):
            page1, page2 = update[i], update[i + 1]
            
            # Check if page1 must come before page2 based on the rules
            if page2 in page_rules.get(page1, []):
                continue  # No violation, pages are in correct order
            elif page1 in page_rules.get(page2, []):
                # Violation: page1 should come after page2, so swap them
                update[i], update[i + 1] = update[i + 1], update[i]
                ordered = False  # Set ordered to False to repeat the check
        
    return update
safe_score = 0
updated_list_score = 0
for test in page_updates:
    if is_safe_update(test):
        #THis might need to account for odd/even
        safe_score +=  test[len(test)//2]   
    else:
        update = reorder_update(test, page_rules)
        updated_list_score += update[len(update)//2]
        
        #updated_list_score += test[len(test)//2]   
print(updated_list_score)