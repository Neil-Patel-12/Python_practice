"""
-> Strings are sequences of characters
-> Strings are immutable.
-> They are defined by enclosing characters in quotes 
   (single, double, triple)
-> Strings support indexing and slicing.
-> They can be concatenated using the + operator.
-> Strings allow repetition using the * operator.
-> They support membership tests with 'in' and 'not in'.
-> interable
"""

# <---- Strings Basics ---->
print("\n<---- Strings Basics ---->")

bird = "Everything looks good from a far"

print(bird)
print(bird[0])

for char in bird:
    print(char, end='')

print()
print(len(bird)) # built-in function

# membership test
print("far" in bird)
print("hello" not in bird)


# <------ Slice ------>
print("\n<------ Slice ------>")

Alphabet = "abcdefghijklmnopqrstuvwxyz"

print(Alphabet[-6])  # "u"
print(Alphabet[2:8])  # "cdefgh"
print(Alphabet[1:])  # "bcdefghijklmnopqrstuvwxyz"
print(Alphabet[:9])  # "abcdefghi"
print(Alphabet[-6:-1])  # "uvwxy"
print(Alphabet[::2])  # "acegikmoqsuwy"
print(Alphabet[::-1])  # "zyxwvutsrqponmlkjihgfedcba"


# <------ built-in methods ------>
print("\n<------ built-in methods ------>")

comment = "   The solar system needs to be explored   "
print(comment.upper())
print(comment.lower())
print(comment.strip())   # removes white space
print(comment.replace("e", "#"))

arr5 = comment.split(" ")
print(arr5)

# letters and numbers
s = "abc123"
print(s.isalnum())  # Output: True

s = "abc123!"
print(s.isalnum())  # Output: False

# alphabetic
k = "abc"
print(k.isalpha())  # Output: True

k = "abc123"
print(k.isalpha())  # Output: False

# numbers
m = "123"
print(m.isdigit())  # Output: True

m = "123abc"
print(m.isdigit())  # Output: False

"""
islower(), isupper(), isspace(), 
"""

home_info = [
    "5 bedrooms", 
    "4 baths", 
    "3500 sq ft", 
    "2-car garage", 
    "Built in 2005"
]

csv_HI_string = ",".join(home_info)
print(csv_HI_string)


# <------ Concatenation ------>
print("\n<------ Concatenation ------>")

a = "how are "
b = "you doing?"
c = a + b
d = "5" * 3
e = "hey " * 5
print(c)
print(d)
print(e)


# <------ F-string ------>
print("\n<------ F-string ------>")

""" Python 3.6 """

age = 36.589
txt = f"My name is John, I am {age}"
print(txt)
print(f"Wow! He is {age:.2f} years old!")


# <---- ord() and chr() ---->
print("\n<------ ord() and chr() ------>")
print(ord("A"))  # Unicode code
print(ord("a"))
print(ord("b"))

print(chr(97))   # returns char for that code
print(chr(98))

