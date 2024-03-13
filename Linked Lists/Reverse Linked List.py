def reverseList(self, head):
        # Use two pointers: prev-curr
        # T O(n), Space - O(1)
    prev, curr = None, head # Initialize pointers
    while curr: # Check if node exists
        nxt = curr.next # Temp. var to have next value
        curr.next = prev # Setting pointer of curr value to previous
        prev = curr # Move prev pointer to curr
        curr = nxt # Move curr pointer to next
    return prev # Return the whole restructured node