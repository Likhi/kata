# Sudoku Solution Validator
# https://www.codewars.com/kata/529bf0e9bdf7657179000008

import copy

def valid_solution(board):
    result = True
    
    # check rows and columns
    for i in range(0,9):
        row = copy.deepcopy(board[i]) # a row
        col = copy.deepcopy([r[i] for r in board])
        
        row.sort() # sort row ascending
        col.sort()

        # check row is 1-9 and col is 1-9
        result &= row == list(range(1,10))
        result &= col == list(range(1,10))
    
    #check inner 3x3
    for m in range(0,9,3):
        for n in range(0,9,3):
            seq = [board[i][n:n+3] for i in range(m,m+3)]
            seq = [item for sublist in seq for item in sublist]
            seq.sort()
            
            # check the 3x3 is 1-9
            result &= seq == list(range(1,10))
    return result

test1 = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
         [6, 7, 2, 1, 9, 5, 3, 4, 8], 
         [1, 9, 8, 3, 4, 2, 5, 6, 7], 
         [8, 5, 9, 7, 6, 1, 4, 2, 3], 
         [4, 2, 6, 8, 5, 3, 7, 9, 1], 
         [7, 1, 3, 9, 2, 4, 8, 5, 6], 
         [9, 6, 1, 5, 3, 7, 2, 8, 4], 
         [2, 8, 7, 4, 1, 9, 6, 3, 5], 
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

test2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
         [6, 7, 2, 1, 9, 0, 3, 4, 9], 
         [1, 0, 0, 3, 4, 2, 5, 6, 0], 
         [8, 5, 9, 7, 6, 1, 0, 2, 0], 
         [4, 2, 6, 8, 5, 3, 7, 9, 1], 
         [7, 1, 3, 9, 2, 4, 8, 5, 6], 
         [9, 0, 1, 5, 3, 7, 2, 1, 4], 
         [2, 8, 7, 4, 1, 9, 6, 3, 5], 
         [3, 0, 0, 4, 8, 1, 1, 7, 9]]

print("Result: ", valid_solution(test1))
print("Result: ", valid_solution(test2))
