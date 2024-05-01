# Because we are given Binary Search Tree we can use it's property
# All value on the left of node is smaller, and all values on the right are greater
# Time complexity(O log n)
# Space - O(1)

def lowestCommonAncestor(root,p,q):
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            cur = cur.right
        elif p.val < curr.val and q.val < curr.val:
            cur = cur.left
        else:
            return cur
