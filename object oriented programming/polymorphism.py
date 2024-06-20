# A key principle in OOP is the idea of polymorphism - and object
# can take on many (poly) forms (morph).

"""
important practical applications:
1. The same class method works in a similar way for different classes
Cat.speak()   # meow
Dog.speak()   # woof
Human.speak()   # hello

-> A common implementation of this is to have a method in a base
(or parent) class that is overridden by a subclass. This is called 
method overriding

-> Each subclass will have a different implementation of the method.
-> if the method is not implemented in the subclass, the version in the
parent class is called is called instead.

2. The same operation works for different kinds of objects
len(iterable)
8 + 2 = 10
"8" + "2" = "82"
"""