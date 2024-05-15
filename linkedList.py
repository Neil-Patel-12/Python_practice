# singular Linked List
# add/insert: beginning, middle, end
# remove/delete: beginning, middle, end
# traversal

# 21

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def is_empty(self):
		if self.head == None:
			return True
		return False

	def get_size(self):
		return self.size

	def traversal(self):
		# if list is empty
		if self.head == None:
			print("Linked List is empty.")
		# if not empty
		else:
			temp = self.head
			while temp != None:
				print(f"{temp.data} --> ", end='')
				temp = temp.next
			print(temp)

	def add_begin(self, value):
		newNode = Node(value)
		if self.is_empty():
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode
		self.size += 1

	def add_end(self, value):
		newNode = Node(value)
		if self.is_empty():
			self.head = newNode
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			temp.next = newNode
		self.size += 1

	def add_at_index(self, value, index):
		newNode = Node(value)
		temp = self.head
		count = 1
		while count != index:
			temp = temp.next
			count += 1
		newNode.next = temp.next
		temp.next = newNode
		self.size += 1

	def delete_begin(self):
		if self.is_empty():
			print("Linked List is empty.")
		else:
			self.head = self.head.next
			self.size -= 1

	def delete_end(self):
		if self.is_empty():
			print("Linked List is empty.")
		elif self.head.next == None:
			self.head = None
			self.size -= 1
		else:
			temp = self.head
			while temp.next.next != None:
				temp = temp.next
			temp.next = None
			self.size -= 1

	def delete_at_index(self, index):



l = LinkedList()
running = False

print("1. add_begin(#)\n2. add_at_index(#, index)\n3. add_end(#)")
print("4. delete_begin()\n5. delete_at_index(index)\n6. delete_end()")

while running:
	option = int(input("Select an option (1-6)"))

	if option == 1:
		val = int(input("Enter a value to add: "))
		l.add_begin(val)

	elif option == 2:
		val = int(input("Enter a value to add: "))
		print("This is a 0-based Linked List")
		if l.get_size() <= 1:
			print(f"Linked List size of ({l.get_size()}) is too small for this operation.")
			continue
		else:
			index = int(input(f"Pick and index between (1-{l.get_size()-2})"))
			l.add_at_index(val, index)

	elif option == 3:
		val = int(input("Enter a value to add: "))
		l.add_end(val)

	elif option == 4:
		l.delete_begin()

	elif option == 5:
		print("This is a 0-based Linked List")
		if l.get_size() <= 2:
			print(f"Linked List size of ({l.get_size()}) is too small for this operation.")
			continue
		else:
			index = int(input(f"Pick and index between (1-{l.get_size()-2})"))
			l.add_at_index(val, index)

	elif option == 6:
		l.delete_end()



l.add_begin(5)
l.add_begin(10)
l.add_begin(15)
l.add_begin(20)

l.add_end(1)
l.add_end(2)
l.add_end(3)

l.add_at_index(100, 3)
l.add_at_index(200, 4)
l.add_at_index(300, 5)
l.add_at_index(999, 1)
l.traversal()

