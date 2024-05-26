# pronounced too-pul or tupple. anything is good
# An order collection or grouping of items!

number = (1, 2, 3, 1, 2, 3, 3, 5, 2)  # But it's immutable! ( cannot be changed )

# cannot update or change values in tuples

if 3 in number:
    print("3 is in number")
# number[2] = 100  TypeError

# why use tuples?
# because Tuples are faster than list
# it makes your code safer
# valid key in dictionaries ( cannot use list as a key in a dict )
# commonly used for UNCHANGED data
# we can have duplicate data

months = (
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
)

# <---- creating / accessing ---->
print("\n<---- creating / accessing ---->")

newTuple = tuple()
another = ()

print(months[5])
print(months[-1])

places = {
    (35.6895, 39.6917): "Tokyo",
    (40.7128, 74.0060): "New York",
    (37.7749, 122.4194): "San Francisco"
}
print(places[(35.6895, 39.6917)])

animals = {"name": "Biscuit", "age": 1.2, "fav_toy": "swing"}
animals.items()
# dict_items([("name", "blue"), ("age", 1.2), ("fav_toy", "swing")])
#                   tuple^^      # tuple^^      # tuple^^
print(animals)

# <---- looping / methods ---->
print("\n<---- looping / methods ---->")

for i in range(len(months)-1, -1, -1):
    print(months[i])

print(number.count(3))
print(number.index(5))  # give index of where it was first found
print(len(number))

anotherTuple = (5, 6, 8, (1, 2), 4, 5, 6, 4, 8, 5, 6, 9, 7, 5)
print(anotherTuple[5:])
print(anotherTuple[3][0])

