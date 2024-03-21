def isSubTree(self, root, subRoot):
    string_t = self.traverse_tree(root)
    string_s = self.traverse_tree(subRoot)

    return string_t in string_s

def traverse_tree(self, node):
    if node is None:
        return "None"
    
    return "#" + str(node.val) + self.traverse_tree(node.left) + self.traverse_tree(node.right)
