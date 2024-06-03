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
	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal):
	pass

blue = Cat()
blue.make_sound("MEOOOWWWAAA")
print(blue.cool)
print(Cat.cool)
print(Animal.cool)
print(isinstance(blue, Animal))