from setup.get_input import fetch_aoc_input
import re
try:
    input_text = fetch_aoc_input(4)
except Exception as e:
    print(e)
print(input_text[0])

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
def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),    # Left to Right
        (0, -1),   # Right to Left
        (1, 0),    # Top to Bottom
        (-1, 0),   # Bottom to Top
        (1, 1),    # Diagonal Down-Right
        (-1, -1),  # Diagonal Up-Left
        (1, -1),   # Diagonal Down-Left
        (-1, 1)    # Diagonal Up-Right
    ]

    def search_direction(row, col, direction):
        for i in range(word_len):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            if not (0 <= new_row < rows and 0 <= new_col < cols) or grid[new_row][new_col] != word[i]:
                return False
        return True

    score = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == word[0]:  # Optimization: Check only if first letter matches
                for direction in directions:
                    if search_direction(row, col, direction):
                        score += 1
    return score

word_to_find = "XMAS"
xmas_input = input_text.splitlines()
score = find_word(xmas_input, word_to_find)
print("Score:", score)




