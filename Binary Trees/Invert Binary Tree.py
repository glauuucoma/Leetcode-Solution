def invertTree(self, root):
    # Depth first search
    # Recursive solution

    # Base case

    if not root:
        return None
    
    # Swap the children

    tmp = root.left # Temp variable to keep left's pointer
    root.left = root.right # Left is right
    root.right = tmp # Right points at left (use temp)

    self.invertTree(root.right) # Call function on both left and right pointers
    self.invertTree(root.left)

    return root # Return root with inverted stuff