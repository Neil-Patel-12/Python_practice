# Going to create a binary search tree in Python

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BST:
	def __init__(self):
		self.root = None

	def insert(self, val):
		if self.root is None:
			self.root = TreeNode(val)
		else:
			self._insert(self.root, val)

	def _insert(self, curr, val):
		if val < curr.val:
			if curr.left is None:
				curr.left = TreeNode(val)
			else:
				self._insert(curr.left, val)
		elif val > curr.val:
			if curr.right is None:
				curr.right = TreeNode(val)
			else:
				self._insert(curr.right, val)
		else:
			print("Value already in Tree.")

	def print_inorder(self):
		if self.root is not None:
			self._print_inorder(self.root)
		else:
			print("Tree is empty")
		print()

	def _print_inorder(self, curr):
		if curr != None:
			self._print_inorder(curr.left)
			print(curr.val, end=' -> ')
			self._print_inorder(curr.right)

	def print_preorder(self):
		if self.root is not None:
			self._print_preorder(self.root)
		else:
			print("Tree is empty")
		print()

	def _print_preorder(self, curr):
		if curr != None:
			print(curr.val, end=' -> ')
			self._print_preorder(curr.left)
			self._print_preorder(curr.right)

	def print_postorder(self):
		if self.root is not None:
			self._print_postorder(self.root)
		else:
			print("Tree is empty")
		print()

	def _print_postorder(self, curr):
		if curr  != None:
			self._print_postorder(curr.left)
			self._print_postorder(curr.right)
			print(curr.val, end=' -> ')

	def height(self):
		if self.root != None:
			return self._height(self.root, 0)
		else:
			return 0

	def _height(self, curr, curr_height):
		if curr == None:
			return curr_height

		left_height = self._height(curr.left, curr_height + 1)
		right_height = self._height(curr.right, curr_height + 1)

		return max(left_height, right_height)

	def search(self, val):
		if self.root != None:
			return self._search(self.root, val)
		else:
			return False

	def _search(self, curr, val):
		if curr.val == val:
			return True
		elif val < curr.val and curr.left != None:
			return self._search(curr.left, val)
		elif val > curr.val and curr.right != None:
			return self._search(curr.right, val)
		return False

	def breath_first_search(self):
		from queue import Queue

		if self.root == None:
			print("Tree is empty")
			return

		q = Queue()
		q.put(self.root)

		while not q.empty():
			levelSize = q.qsize()
			for i in range(levelSize):
				item = q.get()
				print(item.val, end='=')
				if item.left != None:
					q.put(item.left)
				if item.right != None:
					q.put(item.right)
			print()

	def remove(self, val):
		if self.root != None:
			return self._remove(self.root, val)
		else:
			return root

	def _remove(self, root, val):
		if root == None:
			return root
		elif val < root.val:
			root.left = self._remove(root.left, val)
		elif val > root.val:
			root.right = self._remove(root.right, val)
		elif val == root.val:

			if not root.left and not root.right:
				root = None

			elif root.left:
				root.val = self.predecessor(root)
				root.left = self._remove(root.left, root.val)

			elif root.right:
				root.val = self.successor(root)
				root.right = self._remove(root.right, root.val)
		return root

	def predecessor(self, root):
		root = root.left
		while root.right != None:
			root = root.right
		return root.val

	def successor(self, root):
		root = root.right
		while root.left != None:
			root = root.left
		return root.val





def fill_tree(tree, max_elems=100, max_int=1000):
	from random import randint
	for i in range(max_elems):
		randVal = randint(0, max_int)
		tree.insert(randVal)
	return tree



tree = BST()
# tree = fill_tree(tree)
tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)

tree.print_inorder()
tree.print_preorder()
tree.print_postorder()

print(tree.height())

print(tree.search(7))
print(tree.search(8))

tree.breath_first_search()

tree.remove(1)
tree.print_inorder()

# newNode = TreeNode(10)

# print(newNode)
# print(newNode.val)
# print(newNode.left)
# print(newNode.right)