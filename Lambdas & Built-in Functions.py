import sys


def square(num):
    return num * num


print(square(9))  # 81

square2 = lambda num: num * num
add = lambda a, b: a + b

print(square2(7))  # 49
print(add(2, 5))  # 7

print(square.__name__)
print(square2.__name__)
print(add.__name__)


# map: A standard function that accepts at least two arguments, a function and an "iterable"
# iterable - something than can be iterated over (list, strings, dictionaries, sets, tuples)
# map: runs the lambda for each value in the iterable and returns a map object which can be
# converted into another data structure

def decrement_list(arr):
    new_arr = list(map(lambda x: x - 1, arr))
    return new_arr

def extract_full_name(l):
    return list(map(lambda val: f"{val['first']} {val['last']}", l))


nums = [2, 4, 6, 8, 10]
double = map(lambda x: x * 2, nums)  # map object that hold [4, 8, 12, 16, 20]
mapObjectList = list(double)  # or list(map(lambda x: x*2, nums))
print(mapObjectList)

names = [{"first": "Neil", "last": "Patel"},
         {"first": "Deep", "last": "Smart"},
         {"first": "Raj", "last": "plane"}
         ]
first_name = list(map(lambda name: name["first"].upper(), names))
print(first_name)


# filter: There is a lambda for each value in the iterable.
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda

def remove_negatives(arr):
    # remove negative numbers
    new_arr = list(filter(lambda x: x >= 0, arr))
    return new_arr


myList = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, myList))
print(evens)

names = ["Lassie", "Colt", "Rusty", "Rob", "Nick"]
names_less_than_5 = list(map(lambda name: f"Your less than 5 {name}",
                             filter(lambda value: len(value) < 5, names)))
print(names_less_than_5)

# all: Return True if all elements of the iterable are truthy (or if iterable is empty)
# any: Return True if any element of the iterable is truthy. it iterable is empty, r False

all([0, 1, 2, 3])  # False
people = ["Charlie", "Cohn", "Cormen", "Cathryn"]
print(all([name[0] == "C" for name in people]))

any([0, 1, 2, 3])  # True
people.append("Luke")
print(any([name[0] == "C" for name in people]))

# for any and all: use generator expressions if you are not storing the array
list_com = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))
print(f"List Comprehension: {list_com} bytes")
print(f"Generator Expression: {gen_exp} bytes")

# sorted: Returns a new sorted list from the items in iterable
more_numbers = [6, 1, 8, 2]
sorted(more_numbers)  # [1, 2, 6, 8]
print(more_numbers)  # [6, 1, 8, 2]
sorted(more_numbers, reverse=True)

users = [
    {"username": "samuel", "tweets": ["i love cake", "wow"]},
    {"username": "katie", "tweets": ["congratulations"]},
    {"username": "jeff", "tweets": []},
    {"username": "doggo", "tweets": ["dogs are cool"]}
]

another1 = sorted(users, key=lambda user: user["username"])
another2 = sorted(users, key=lambda user: len(user["tweets"]))

# max: Return the larges item in an iterable or the larges of two or more arguments.
# min is the opposite
print(max(3, 66, 99))
print(max('c', 'g', 'k'))
print(max([3, 2, 4, 1]))
print(max((1, 5, 9, 6)))
print(max("awesome"))
print(max({1: 'a', 3: 'c', 2: 'b'}))

names2 = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
most_char = max(len(name) for name in names2)  # Generator Expression
name_with_most_char = max(names2, key=lambda n: len(n))

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

least_played_song = min(songs, key=lambda s: s["playcount"])
best_song = max(songs, key=lambda s: s["playcount"])["title"]

# reversed: Return a revers iterator
# this will reverse any iterator
nuns = [1, 2, 3, 4]
nuns.reverse()  # reverse() only works with list Permanent
print(nuns)

print(list(reversed(nuns)))  # nuns = [4, 3, 2, 1]

for char in reversed("hello world"):
    print(char)
for i in reversed(range(0, 10)):
    print(i)

# len: return the length      they all have a __len__() dunder
# accept a sequence such as (list, string, tuple, range)
# accept a collection such as (dict or set)


# abs: Return the absolute value of a num. The argument may be an integer or a float
# def: the magnitude of a real number without regard to its sign

print(abs(-2))
print(abs(-03256.454))
print(abs(-78))
print(abs(float("40")))

simple_list = [4, 5, 6]
print(sum(simple_list))

print(round(10.2))  # 10
print(round(10.5))  # 11
print(round(1.212121, 2))  # 1.21




# zip: Make an iterator that aggregates elements from each of the iterables
# Returns an iterator of tuples, where the i-th tuple contains the i-th element of each sequence
# The iterator stops when the shortest input iterable is exhausted
# remember, zip will return a list of paired tuples

def interleave(str1, str2):
    # return a new string containing the 2 strings interwoven
    newstr = ''
    for i in zip(str1, str2):
        newstr += i[0] + i[1]

    return newstr

first_zip = list(zip([1, 2, 3], [4, 5, 6]))  # [(1, 4), (2, 5), (3, 6)]

back_together = list(zip(*first_zip))  # [(1,2,3), (4,5,6)]

midterms = [80, 91, 78]
finals = [98, 89, 78]
students = ["dan", "ang", "kate"]

# returns dict with {student:"highest score"} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:"highest score"} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student: "average score"
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)