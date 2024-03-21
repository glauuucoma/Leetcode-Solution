def hasCycle(self, head):
    if not head or not head.next:  # if head or next attr doesnt exist
        return False # no cycle - return false

    visited = set()  # Use a set to store visited nodes
    curr = head # curr is head
    while curr: # while current exists
        if curr in visited: # if current is visited
            return True # it's cycle
        visited.add(curr) # add curr node to visited
        curr = curr.next # move pointer
    return False # return false