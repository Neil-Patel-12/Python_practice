# lists are implemented as dynamic arrays internally.

# the items in a list can be ordered, changeable, and allows duplicate values
# the order can stay the same or change/ list can change, add, & remove items

mylist = ["apple", "banana", "cherry", "orange", "grapes", "blueberry"]
print(mylist)

number = len(mylist)
print(number)

initialize_array = [1] * 5

list1 = ["father", "mother", "sister", "brother"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
list5 = list()
list6 = list((10, 20, 30, 40, 50, 60))
list7 = list(range(1, 11))

print(type(list6))




# <---- Access List Items ---->
print("\n<---- Access List Items ---->")

animals = ["cat", "dog", "horse", "lion", "elephant", "bear"]
print(animals[1])
print(animals[-2])
print(animals[2:5])
print(animals[:4])
print(animals[2:])
print(animals[-4:-1])
if "lion" in animals:  # O(n)
    print("Yes, Lion is in the list.")
for i in range(0, len(animals)):
    print(animals[i])




# <---- Change List Items ---->
print("\n<---- Change List Items ---->")

cars = ["Ford", "BMW", "Mercury", "Audi", "Bentley"]
cars[0] = "Koenigsegg"
cars[1:3] = ["McLaren", "Porsche"]
cars.insert(3, "Lamborghini")
print("the cars are: ", cars, " the size of the array is: ", len(cars))




# <---- Add List Items ---->
print("\n<---- Add List Items ---->")

nums = [9, 6, 3, 8, 5, 2, 0, 7, 4, 1]
nums.append(10)

nums.insert(3, 20)

nums.extend([60, 70, 80, 90])  # can add any iterable object (tuples, sets, dictionaries etc.)
nums.extend("Neil Patel")

print(nums)




# <---- Remove List Items ---->
print("\n<---- Remove List Items ---->")

color = ["yellow", "red", "green", "red", "blue", "purple", "pink", "white"]
color.remove("red")  # removes the specified item # will remove the first occurrence
color.pop()  # removes the last item
color.pop(-1)  # remove the specified index
del color[3]  # remove the specified index
color.clear()  # delete everything inside the list, list still remains.
del color  # delete the entire array




# <---- Loop Lists ---->
print("\n<---- Loop Lists ---->")

for car in cars:
    print(car, end=", ")
print()

for i in range(len(cars)):
    print(f"{i}: {cars[i]}")
print()

for i, car in enumerate(cars):
    print(i, car)

[print(x) for x in cars]  # List Comprehension




# <---- List Comprehension ---->
print("\n<---- List Comprehension ---->")

# [ ___ for ___ in ___ ]
triple = [(i*3) for i in range(11)]
print(triple)

closePeople = ["deep", "raj", "kush", "aria"]
# betterPeople = [closePeople[i][0].upper() + closePeople[i][1:] for i in range(len(closePeople))]

betterPeople = [(ppl[0].upper() + ppl[1:])for ppl in closePeople]
print(betterPeople)

falsyyy = [bool(val) for val in [0, [], "", 66]]
print(falsyyy)

# CONDITIONAL LOGIC IN LIST COMPREHENSION
moreNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenNum = [val for val in moreNumber if val % 2 == 0]

oddNum = [num**2 if num % 2 == 0 else num**3 for num in moreNumber]




# <---- List Methods ---->
print("\n<---- List Methods ---->")

data = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9]
data.append(100)
data.append([9, 8, 7])  # can add anything to the end
data.insert(4, 200)
# data.extend("hello there")   # can add anything that is iterable

data.pop()   # removes and return the item that is removed
data.pop(1)   # removes and return the item that is removed
data.remove(4)
# data.clear()

data.index(1)  # it's at position 0
data.index(1, 3)  # start at 3
data.count(1)  # how many 1s are there?

data.reverse()  # reverse the list in place
data.sort()
data.sort(reverse=True)
newData = sorted(data)

iPhone = ["6", "7", "8", "10", "11", "12", "13", "14", "15"]
phoneString = ' '.join(iPhone)
print(phoneString)
print(type(phoneString))

print(data)




# <---- List SLICE ---->
print("\n<---- List SLICE ---->")

arr77 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr77[::-1])

print(arr77[1::2])

print(arr77[len(arr77)::-1])

print(arr77[::-2])
print(arr77[2::-1])
print(arr77[5:0:-1])

arr77[0], arr77[1] = arr77[1], arr77[0]
print(arr77)




# <---- Nested List ---->
print("\n<---- Nested List ---->")

nested = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]
]

# this is unpacking to variable, useful for pairs
x, y, z = [10, 20, 30]