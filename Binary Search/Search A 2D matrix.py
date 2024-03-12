class Solution(object):
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                l, r = 0, COLS - 1
                while l <= r:
                    m = (l + r) // 2
                    if target > matrix[row][m]:
                        l = m + 1
                    elif target < matrix[row][m]:
                        r = m - 1
                    else:
                        return True
                return False
    
        return False 


        