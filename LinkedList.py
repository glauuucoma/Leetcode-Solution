# Linked List example

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

	def get_data(self):
		return self.val

	def set_data(self, val):
		self.val = val

	def get_next(self):
		return self.next

# After we would set up Node object we can create LinkedList class

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.count = 0

	def get_count(self):
		return self.count

	def insert(self, data): #Insert in the end
		#TO-DO insert a new node
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		self.count += 1

	def find(self, val):
		#TO-Do: find the first item with a given value
		item = self.head

		return None


