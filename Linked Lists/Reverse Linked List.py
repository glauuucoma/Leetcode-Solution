def reverseList(self, head):
    prev, curr = None, head

    while curr:
        nxt = curr.next # Temprorarily variable
        curr.next = prev
        prev = curr
        curr= nxt
    return prev

# Break down

# Initialize previous and current Node
# Previous is None and the curr is head
# While node exists:
# Next node is curr.next property
# 