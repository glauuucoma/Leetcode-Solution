def isValidBST(self, root: TreeNode) -> bool:

    def valid(node,left,right):
        if not node: #If node is not null
            return True
        if not(node.val < right and node.val > left):
            return False
            
        return(valid(node.left, left, node.val) and
        valid(node.right, node.val, right))
    return valid(root, float("-inf"), float("inf"))
