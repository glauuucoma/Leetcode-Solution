# We need n open parenthesis and closing parenthesis
# We can start only with open
# We can add more parenthesis if open < n
# valid IIF open == closed == n
class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
                if openN == closedN == n:
                    res.append("".join(stack))
                    return

                if openN < n:
                    stack.append("(")
                    backtrack(openN + 1, closedN)
                    stack.pop()
            
                if closedN < openN:
                    stack.append(")")
                    backtrack(openN, closedN + 1)
                    stack.pop()
    
        backtrack(0,0)
        return res
        

inst = Solution()
print(inst.generateParenthesis(2))