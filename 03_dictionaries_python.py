# <---- create a dictionary ---->
print("\n<---- create a dictionary ---->")

cat = {"name": "Blue", "age": 3.5, "runner": True}
bird = {}
monkey = dict()
green = dict(tree=True)
green2 = dict(tree=True, grass=True)
print(green)

my_dict1 = defaultdict(list)
my_dict2 = defaultdict(int)

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

total_donations_2 = sum(donation for donation in donations.values())
total_donations_3 = sum(donations.values())
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
# d.clear()   d still exist, its just empty now    ex. {}
c = d.copy()
checking_location = c is d  # False

newDict1 = dict().fromkeys(['email', 'name', 'profile', 'score'], 'unknown')
newDict2 = {}.fromkeys("a", [1, 2, 3, 4])
newDict3 = {}.fromkeys(['phone'], 'unknown')
newDict4 = dict().fromkeys(range(1, 10), 'good')

print(newDict4)

# get: returns None is key is not in the dictionary
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

dValue = d.pop('a')  # pops the key-value pair from dict and returns the value
# dValue2 = d.pop('e')  # KeyError

willGetRideOfARandomKey = d.popitem()

# update
first = dict(a=1, b=2, c=3, d=4, e=5, f=6)
second = {}
second.update(first)
second.update({'a': 6, 'c': 9, 'e': 50})

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

# <---- dictionaries Comprehension chr(num) = char ---->
print("\n<---- dictionaries Comprehension ---->")

ASCII = {letter: chr(letter) for letter in range(65, 91)}