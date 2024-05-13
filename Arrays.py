# built-in array methods

# Python lists are one of the most versatile data structures in the language, and
# they come with a wide range of built-in methods. These methods can be used to
# perform a variety of tasks, such as adding, removing, sorting, and searching lists.

# <-------------- Creating a list -------------->
myArray = [1, 2, 3, 4, 5, 6, 7, 8]

# list(): constructor to create another list from an iterable object
list2 = list((10, 20, 30, 40, 50, 60, 70, 80, 90))
list3 = list("hello world")
list4 = list(range(0, 10))

list_comprehension = [i for i in range(0, 20, 5)]
list_comprehension2 = list(x for x in range(6, 10))

simple_list = []
simple_list.append(1.5)
simple_list.append(2.5)
simple_list.append(3.5)

new_simple_list = [0] * 5

print(myArray)
print(list2)
print(list3)
print(list4)
print(list_comprehension)
print(list_comprehension2)
print(simple_list)
print(new_simple_list)
# <-------------- Creating a list -------------->


# <-------------- adding elements to a list -------------->
# 𝚊𝚙𝚙𝚎𝚗𝚍(): Add an item to the end of the list.
myArray.append(9)
myArray.append("string")
myArray.append(True)
myArray.append((55, 66, 77))
myArray.append([100, 200, 300])
print(myArray)

# 𝚒𝚗𝚜𝚎𝚛𝚝(): Insert an item at a specific index in the list.
myArray.insert(2, 99)
print(myArray)

# 𝚎𝚡𝚝𝚎𝚗𝚍(): Add the elements of another (iterable object) to the end of the list.
twoList = [22, 33, 44]
myArray.extend(twoList)
print(myArray)