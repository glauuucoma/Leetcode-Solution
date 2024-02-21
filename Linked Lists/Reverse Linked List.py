def reverseList(self, head):
    prev, curr = None, head

    while curr:
        nxt = curr.next # Temprorarily variable
        curr.next = prev
        prev = curr
        curr= nxt
    return prev

# recursive Solution

def reverseListRecur(self, head):
    if not head:
        return None
    
    newHead = head

    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None
    return newHead