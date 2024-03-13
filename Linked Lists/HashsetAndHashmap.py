# 705. Design a Hashset
# add(key)
# remove(key)
# contains(key)

# Handle collisions using linked list

# To set index of the key we will use mod operator
# key % n = index
# n = max_size of the array
# This way we will prevent array from containing
# over 10 000 of elements

# Also all the values in the hashset is unique
# So when insert() method would be invoked at first
# We will check whether a value already exists using contains()





class ListNode:
	def __init__(self, key):
		self.key = key
		self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]


    def add(self, key):
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next: # We are referencing the next node cause ListNode(0) is a Dummy Node
        	if cur.next.key == key:
        		return
        	cur = cur.next
        cur.next = ListNode(key)
        

    def remove(self, key):
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next: # We are referencing the next node cause ListNode(0) is a Dummy Node
        	if cur.next.key == key:
        		cur.next = cur.next.next
        		return
        	cur = cur.next
        	
        

    def contains(self, key):
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next: # We are referencing the next node cause ListNode(0) is a Dummy Node
        	if cur.next.key == key:
        		return True
        	cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)