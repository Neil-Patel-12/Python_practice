import sys
def square(num):
    return num * num

print(square(9))  # 81

square2 = lambda num: num * num
add = lambda a,b: a + b

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
    new_arr = list(map(lambda x: x-1, arr))
    return new_arr

nums = [2, 4, 6, 8, 10]
double = map(lambda x: x*2, nums)  # map object that hold [4, 8, 12, 16, 20]
mapObjectList = list(double)   # or list(map(lambda x: x*2, nums))
print(mapObjectList)

names = [ {"first": "Neil", "last": "Patel"},
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
print(all([name[0]=="C" for name in people]))

any([0, 1, 2, 3])  # True
people.append("Luke")
print(any([name[0]=="C" for name in people]))

# for any and all: use generator expressions if you are not storing the array
list_com = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))
print(f"List Comprehension: {list_com} bytes")
print(f"Generator Expression: {gen_exp} bytes")