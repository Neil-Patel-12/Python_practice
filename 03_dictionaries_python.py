from collections import defaultdict

# <---- create a dictionary ---->
print("\n<---- create a dictionary ---->")

cat = {"name": "Blue", "age": 3.5, "runner": True}
bird = {}
monkey = dict()
green = dict(isTree=True, isRed=False, num=5555)
green2 = dict(isCold=True, isGrassGreen=True)

my_dict1 = defaultdict(list)
my_dict2 = defaultdict(int)

my_dict1['fruits'].append('apple')
my_dict1['fruits'].append('banana')
my_dict1['vegetables'].append('carrot')

my_dict2['apple'] += 1
my_dict2['banana'] += 1
my_dict2['apple'] += 1

first = dict([('isTree', True), ('isRed', False), ('num', 99)])
second = dict([('isCold', True), ('isGrassGreen', True)])

print(cat)
print(bird)
print(monkey)
print(green)
print(green2)
print(my_dict1)
print(my_dict2)

print(first)
print(second)

# <---- ACCESSING ---->
print("\n<---- ACCESSING ---->")

instructor = {
    "name": "Neil",
    "owns_bird": False,
    "num_classes": 5,
    "favorite_language": "python",
    "needs_milk": True,
    "fave_num": 55
}

print(instructor["name"])
print(instructor["fave_num"])

# <---- looping over dictionaries ---->
print("\n<---- looping over dictionaries ---->")

for value in instructor.values():
    print(value)

for key in instructor.keys():
    print(key)

for key, value in instructor.items():
    print(f"{key}: {value}")

######
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations_1 = 0

for donation in donations.values():
    total_donations_1 += donation
print("total_donations_1", total_donations_1)

total_donations_2 = sum(donation for donation in donations.values())
total_donations_3 = sum(donations.values())

print("total_donations_2", total_donations_2)
print("total_donations_3", total_donations_3)
######

# <---- test for existence dictionaries ---->
print("\n<---- test for existence dictionaries ---->")

value1 = "age" in instructor
print(value1)
value2 = "name" in instructor
print(value2)
value3 = "Neil" in instructor.values()
print(value3)
value4 = 5 in instructor.values()
print(value4)

# <---- dictionaries methods ---->
print("\n<---- dictionaries methods ---->")

d = dict(a=1, b=2, c=3)
print(d)
# d.clear()   d still exist, its just empty now    ex. {}
c = d.copy()
checking_location = c is d  # False

newDict1 = dict().fromkeys(['email', 'name', 'profile', 'score'], 'unknown')
newDict2 = {}.fromkeys("a", [1, 2, 3, 4])
newDict3 = {}.fromkeys(['phone'], 'unknown')
newDict4 = dict().fromkeys(range(1, 10), 'good')
newDict5 = dict.fromkeys(["red", "orange", "yellow", "green"], 0)

print(newDict1)
print(newDict2)
print(newDict3)
print(newDict4)
print(newDict5)

# get: returns None if key is not in the dictionary
home = {
    "price": 400000,
    "bathrooms": 5,
    "bedrooms": 6,
    "ceilings": "20 feet",
    "floor": "wood"
}
print(home.get("price"))
print(home.get("bathrooms"))
print(home.get("square_feet", "not informed"))
print(home.get("flooring"))

dValue = d.pop('a')  # pops the key-value pair from dict and returns the value
# dValue2 = d.pop('e')  # KeyError
print(dValue)

willGetRidOfARandomKey = d.popitem()  # NEVER USE THIS

# update
first = dict(a=1, b=2, c=3, d=4, e=5, f=6)
second = {}
second.update(first)
second.update({'a': 6, 'c': 9, 'e': 50})

print(first)
print(second)

# <---- dictionaries Comprehension ---->
print("\n<---- dictionaries Comprehension ---->")

# syntax -> { ___:___ for ___ in ___ }
more_nums = dict(frist=1, second=2, third=3)
square_nums = {key: value**2 for key, value in more_nums.items()}
print(square_nums)

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
dict_of_nums = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(dict_of_nums)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

person2 = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer2 = dict(person)

answer3 = {}.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)

answer4 = {vowel: 0 for vowel in ['a', 'e', 'i', 'o', 'u']}

print(answer)
print(answer2)
print(answer3)
print(answer4)

# <---- dictionaries Comprehension chr(num) = char ---->
print("\n<---- dictionaries Comprehension ---->")

ASCII = {letter: chr(letter) for letter in range(65, 91)}
print(ASCII)