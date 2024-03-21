def maxTree(self, root):
    # if not root:
        #     return 0

        # # Recursive - O(n)
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # Iterative 
        # Uses stack DS
    if not root:
        return 0
    
    stack = [[root, 1]]
    res = 1
    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res,depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
        
    return res