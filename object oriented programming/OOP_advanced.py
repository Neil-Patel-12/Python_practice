# OOP_advanced

"""
implement inheritance, including multiple inheritance,
understand method resolution order,
understand polymorphism
add special methods to classes
"""

# inheritance -> a key feature of OOP is the ability 
# to define a class which inherits form another class (a "base" or "parent" class).
# In Python, inheritance works by passing the parent class as an argument to the definition of a child class:
# class Cat(Animal):

class Animal:
	cool = True
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		super().__init__(name, species)
		# Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy
	def play(self):
		print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Cat", "Scottish Fold", "String")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
blue.play()



"""
blue = Cat()
blue.make_sound("MEOOOWWWAAA")

print(blue.cool)
print(Cat.cool)
print(Animal.cool)

print(isinstance(blue, Animal))
print(isinstance(blue, Cat))
print(isinstance(blue, object))
"""
