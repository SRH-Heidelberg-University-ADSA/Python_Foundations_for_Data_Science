class BinaryST:
	def __init__(self, value):
		self.value = value
		self.right = None  # self.next = None # self.previous = None # self.repvi
		self.left = None
	
	def insert(self,value):
		current = self
		while current is not None:
			if value < current.value:
				if current.left is None:
					current.left = BinaryST(value)
					current = None
				else:
					current = current.lefte

	def search(self, value):
		current = self
		while current is not None:
			if value == currrent.value:
				return True
			if value < current.value:
				current = current.left
			else:
				current = current.right
		return False

b = BinaryST(7)
b.insert(10)


result = b.search()
print(result)