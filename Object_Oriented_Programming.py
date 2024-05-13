# class - a blueprint for objects. Contain methods and attributes
# instance - object that are constructed from class blueprint which hava methods and properties

# Encapsulation - the grouping of public & private attributes and methods,
#                 into a programmatic class, making abstraction possible
# Abstraction - exposing only "relavant" data in a class interface, hiding
#               private attributes and methods (aka the "inner workings")
#               from users

# class methods - are methods (with the @classmethod decorator) that are
# not concerned with instances, but the class itself. 
# ^^^^^ used when your crating a new instance of a class 

class User:

	active_users = 0  # this is a class attribute
	allowed = ("Lakeland", "Miami", "Gainesville", "Tampa", "Orlando")

	def __init__(self, first, last, age):
		# instance attributs 
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users}"

	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(",")
		return cls(first, last, int(age))

	def log_out(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		# instance methods
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0].upper()}.{self.last[0].upper()}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th Birthday, {self.first}!!!"


user1 = User("Joe", "william", 87)  # create object that is an instance of a class
user2 = User("Blanca", "Cool", 54)  # is called instantiating a class
print(user2.full_name())
print(user2.initials())
print(user1.likes("Pizza"))
print(user1.is_senior())
print(user2.birthday())

print(User.active_users)
print(user2.log_out())
print(User.active_users)

print(user1.display_active_users())
print(User.display_active_users())

Tom = User.from_string("Tom,Jones,89")  # calling class method