me = "Everything looks good from a far"

print(me)
print(me[0])

for char in me:
    print(char, end='')

print()
print(len(me))

print("from" in me)
print("hello" not in me)

# <------ Slice ------>
print("<------ Slice ------>")

new = "school is fun with python"

print(new[2:8])
print(new[:9])
print(new[1:])
print(new[-6])   # try -1
print(new[-6:-1])
print(new[::-1])

# <------ methods ------>
print("<------ methods ------>")

methods = "The solar system needs to be explored"
print(methods.upper())
print(methods.lower())
print(methods.strip())   # removes white space
print(methods.replace("e", "#"))
arr5 = methods.split(" ")
print(arr5)

# <------ Concatenation ------>
print("<------ Concatenation ------>")

a = "how are "
b = "you doing?"
c = a + b
print(c)

# <------ F-string ------>
print("<------ F-string ------>")

age = 36.589
txt = f"My name is John, I am {age}"
print(txt)
print(f"Wow! He is {age:.2f} years old!")


# <---- ord() and chr() ---->
print(ord("A"))
print(ord("a"))
print(ord("b"))

print(chr(97))
print(chr(98))

