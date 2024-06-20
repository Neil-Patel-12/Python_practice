class User:

	active_users = 0  # this is a class attribute
	allowed = ("Lakeland", "Miami", "Gainesville", "Tampa", "Orlando")

	def __init__(self, first, last, age):
		# instance attributs 
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def __repr__(self):
		return f"{self.first} is {self.age}"

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

class Moderator(User):
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community

	def remove_post(self):
		return f"{self.full_name()} removed a post from the {self.community} community."

mathew = Moderator("Mathew", "King", 22, "football")
print(mathew.remove_post())