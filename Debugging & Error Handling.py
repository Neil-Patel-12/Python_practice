import pdb
first = "First"
second = "Second"
pdb.set_trace()  # here the debugger will start
result = first + second
third = "Third"
result += third
print(result)

# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finished debugging)



# SyntaxError: when python encounters incorrect syntax
# NameError: Occurs when a variable is not defined/ hasn't been assigned
# TypeError: An operation or function is applied to the wrong type
# IndexError: Occurs when you try to access an element in a list using an invalid index
# ValueError: Occurs when a built-in operation or function receives an argument that has...
#     the right type but an inappropriate value   ex. int("foo")
# KeyError: This occurs with dictionary does not have a specific key
# AttributeError: Occurs when a variable does not have an attribute  ex. "awesome".foo


# Raise your own exception! we can also throw errors
# raise ValueError("invalid value")


def colorize(text, color):
    colors = ("red", "orange", "yellow", "green", "blue", "purple")
    if type(text) is not str:
        raise TypeError("text must be a string")
    if type(color) is not str:
        raise TypeError("color must be a string")
    if color not in colors:
        raise ValueError("color is invalid color")
    else:
        print(f"Printed {text} in {color}")


colorize("hello", "red")
# colorize(54, "blue")


# try/ except blocks
try:
    runner()
except NameError:
    print("You tried to use a variable that was never declared!")


# try, except, else, finally
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Good, there was no problem")
        break
    finally:
        print("RUNS NO MATTER WHAT!")
print("end logic")


def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong")
        print(err)
    else:
        print(f"{a} divided {b} us {result}")

print(divide(1, 'a'))
print(divide(1, 0))
