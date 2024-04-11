# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isBalanced(self, root):

    # def dfs(root):
    #     if not root: # Base case
    #         return [True, 0] # Return True because height same, return height

    #     # Call recursion on left and right part
    #     left, right = dfs(root.left), dfs(root.right)
    #     # Balanced if left and right true and height of left - right equals or less than 1
    #     balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

    #     # Return if balanced and determine max height by comparing 
    #     # left and right heights
    #     return [balanced, 1 + max(left[1], right[1])]
    
    # # Call function and get zero index of result
    # return dfs(root)[0]

    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)

        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]
    


    