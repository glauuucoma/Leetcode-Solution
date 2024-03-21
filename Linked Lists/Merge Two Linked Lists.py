def mergeTwoLists(self, list1, list2):
    # 2 Heads - Sorted
    dummy = ListNode() # Creating a dummy node
    tail = dummy # Assigning to tail to dummy

    while list1 and list2: # While both list cur value not null
        if list1.val < list2.val: # If list1 val less than list2 val
            tail.next = list1 # Set next pointer of tail to list1 val
            list1 = list1.next # Move list1 pointer to next value
        else: # Else
            tail.next = list2 # Set next tail pointer to list2 val
            list2 = list2.next # Moove list 2 pointer to next value
        tail = tail.next # Move tail to next val

    if list1: # If list1 exists 
        tail.next = list1 # Tail equals to list1
    elif list2: # Else if list 2 exist
        tail.next = list2 # Tail equls to list2 val

    return dummy.next # Return dummy's pointer to next val