# sets are like formal mathematical sets
# sets do not contain duplicate values
# Elements in sets aren't ordered

# every item in a set is unique
# cannot access using index




# <---- Accessing and Creating ---->
print("\n<---- Accessing and Creating ---->")

s = set({1, 2, 3, 4, 5, 5, 5})

b = {4, 9, 3, 6, 9}

m = {5.5, 'a', 89, "hello", True}

if 9 in b:
    print("very nice")
if True in m:
    print("True is in there")

for thing in m:
    print("<>", thing, end="")




# <---- something cool ---->
print("\n<---- something cool ---->")

places = ['North', 'South', 'West', 'East', 'West', 'North', 'South']
simple = list(set(places))
print(simple)




# <---- Methods ---->
print("\n<---- Methods ---->")

b.add(5)
b.remove(4)  # will throw KeyError if item not in set
b.discard(7)  # will not throw KeyError
another_b = b.copy()  # another_b is b == False
another_b.clear()

# set math ( intersection, symmetric_difference, union )
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# union students
new1 = math_students | biology_students
print(new1)

# both courses
new2 = math_students & biology_students
print(new2)




# <---- Set Comprehension ---->
print("\n<---- Set Comprehension ---->")

check = {x ** 2 for x in range(0, 10)}
next = {char.upper() for char in "runner"}
print(check, next)


def check_all_vowels_in_s(check_string):
    return len({c for c in check_string if c in 'aeiou'}) == 5



# <---- summary ---->
print("\n<---- summary ---->")

myset = set() # {,}
hashset = set([5, 6, 5, 1]) # {6, 1, 5}

myset.add(1)
myset.add(2) # O(1) adding
print(myset)

print(len(myset))
print(2 in myset) # O(1) look up

myset.remove(1) # O(1) removeal