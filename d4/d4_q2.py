from setup.get_input import fetch_aoc_input
import re
try:
    input_text = fetch_aoc_input(4)
except Exception as e:
    print(e)


'''
1. Iterate over the text.
2. If the character is an 'X', we just pass the index to a function that checks the grid for the other characters
If its true, we count it.

Algorith is_xmas(idx, input) 
    left = idx > 4 and input[row][idx-4:idx] == 'XMAS'
    right = idx < len(row) and input[row][idx-4:idx]
    diag_left_to_right_down = idx > 0 and row+3 < len(input) and idx+3 < len(row) and input[row][idx] == 'X' and input[row+1][idx+1] == 'M' and input[row+2][idx+2] == 'A'
    and input[row+3][idx+3] == 'S' 
    diag_left_to_right_up = row-3 > 0 and idx-3 > 0 and input[row][idx] == 'X' and input[row-1][idx-1] == 'M' and input[row-2][idx-2] == 'A'
    and input[row-3][idx-3] == 'S' 
    diag_right_to_left_down = idx > 0 and row+3 < len(input) and idx+3 < len(row) and input[row][idx] == 'X' and input[row+1][idx+1] == 'M' and input[row+2][idx+2] == 'A'
    and input[row+3][idx+3] == 'S' 
    diag_right_to_left_up = row-3 > 0 and idx+3 < len(row) and input[row][idx] == 'X' and input[row-1][idx+1] == 'M' and input[row-2][idx+2] == 'A'
    and input[row-3][idx+3] == 'S' 
    up_to_down = row+3 < len(row) and input[row][idx] == 'X' and input[row+1][idx] == 'M' and input[row+2][idx] == 'A' and input[row+3][idx] == 'S'
    down_to_up = row-3 > 0 and input[row][idx] == 'X' and input[row-1][idx] == 'M' and input[row-2][idx] == 'A' and input[row-3][idx] == 'S'

    if left or right or diag_left_to_right_down or diag_left_to_right_up or diag_right_to_left_down or diag_right_to_left_up or up_to_down
    or down_to_up:
        return True 




'''
def find_xmas(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    score = 0

    def is_xmas_pattern(row, col):
        # Check the center is 'A'
        if grid[row][col] != 'A':
            return False

        # Top-left to bottom-right (MAS/SAM) and Top-right to bottom-left (MAS/SAM)
        tl_br = (grid[row - 1][col - 1], grid[row + 1][col + 1]) in [('M', 'S'), ('S', 'M')]
        tr_bl = (grid[row - 1][col + 1], grid[row + 1][col - 1]) in [('M', 'S'), ('S', 'M')]

        return tl_br and tr_bl

    # Traverse through the grid and check for X-MAS pattern at each potential center
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if is_xmas_pattern(row, col):
                score += 1

    return score
word_to_find = "MAS"
xmas_input = input_text.splitlines()
#xmas_input = "MAS\nSAM\nMAS\nCAS".splitlines()
#print(xmax_input)
print(xmas_input)
score = find_xmas(xmas_input, word_to_find)
print("Score:", score)




