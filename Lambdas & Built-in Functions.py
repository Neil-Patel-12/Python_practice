def square(num):
    return num * num

print(square(9))

square2 = lambda num: num * num
add = lambda a,b: a + b

print(square2(7))
print(add(2, 5))

print(square.__name__)
print(square2.__name__)
print(add.__name__)

