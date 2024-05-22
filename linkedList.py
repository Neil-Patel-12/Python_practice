# singular Linked List
# add/insert: beginning, middle, end
# remove/delete: beginning, middle, end
# traversal
# searching, merging 2 linked list, reverse linked list, sorting linked list, 

class Node:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

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
		if index == 0:
			self.add_begin(value)
			return
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

	def delete_value(self, value):
		temp = self.head
		count = 1
		if temp.data == value:
			self.head = self.head.next
			self.size -= 1
		else:
			while temp.next != None:
				if temp.next.data == value:
					break
				temp = temp.next
			if temp.next == None:
				print(f"value ({value}) not found")
			elif temp.next.data == value:
				temp.next = temp.next.next
				self.size -= 1

	def search(self, value):
		temp = self.head
		count = 0
		while temp != None:
			if temp.data == value:
				print(f"{value} is at index {count}.")
				break
			temp = temp.next
			count += 1
		if count == self.size:
			print(f"{value} not found.")

	def reverse_ll(self):
		# reverse a linked list
		prev = None
		curr = self.head
		up = None
		while curr != None:
			up = curr.next
			curr.next = prev
			prev = curr
			curr = up
		self.head = prev
		print("Reversal is Successful.")

	def sort_linked_list(self):
		sorted_array = []
		temp = self.head
		while temp:
			sorted_array.append(temp.data)
			temp = temp.next
		print(sorted_array)
		sorted_array.sort()
		dummy = Node()
		tail = dummy
		length = len(sorted_array)

		i = 0
		while length > 0:
			tail.next = Node(sorted_array[i])
			tail = tail.next
			i += 1
			length -= 1
		self.head = dummy.next

def merge_2_sorted_linked_list(list1, list2):
	dummy = Node()
	tail = dummy
	while list1 and list2:
		if list1.data < list2.data:
			tail.next = list1
			list1 = list1.next
		else:
			tail.next = list2
			list2 = list2.next
		tail = tail.next

	if list1:
		tail.next = list1
	if list2:
		tail.next = list2
	return dummy.next

def print_ll(head):
	temp = head
	while temp:
		print(temp.data, end=" -> ")
		temp = temp.next


l = LinkedList()
running = True

print()
print("1. add_begin(#)\n2. add_at_index(#, index)\n3. add_end(#)")
print("4. delete_begin()\n5. delete_value(#)\n6. delete_end()")
print("7. search()\n8. reverse_ll()\n9. sort_ll()")
print()

while running:
	option = int(input("Select an option (1-6): "))

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
			index = int(input(f"Pick and index between (0-{l.get_size()}): "))
			l.add_at_index(val, index)

	elif option == 3:
		val = int(input("Enter a value to add: "))
		l.add_end(val)

	elif option == 4:
		l.delete_begin()

	elif option == 5:
		val = int(input("Enter a value to delete: "))
		l.delete_value(val)

	elif option == 6:
		l.delete_end()

	elif option == 7:
		val = int(input("Enter a value to search: "))
		l.search(val)

	elif option == 8:
		l.reverse_ll()

	elif option == 9:
		l.sort_linked_list()

	elif option == 99:
		running = False

	l.traversal()
	print()



# l.add_begin(5)
# l.add_begin(10)
# l.add_begin(15)
# l.add_begin(20)

# l.add_end(1)
# l.add_end(2)
# l.add_end(3)

# l.add_at_index(100, 3)
# l.add_at_index(200, 4)
# l.add_at_index(300, 5)
# l.add_at_index(999, 1)
# l.traversal()


# TESTING /// merge_2_sorted_linked_list():

# Example list1: 1 -> 4 -> 5
list1 = Node(2)
list1.next = Node(4)
list1.next.next = Node(5)

# Example list2: 3 -> 4 -> 8
list2 = Node(3)
list2.next = Node(4)
list2.next.next = Node(8)

newhead = merge_2_sorted_linked_list(list1, list2)

print_ll(newhead)