class MyClass:
    # A class attribute
    x = 5


class Person:
    # Another class attribute
    name = "John"


class Point:
    x = 0
    y = 0


class Lamp:
    on = False


class Book:
    title = "Unknown"


# Example 1: Create object and access attribute
obj = MyClass()
print(obj.x)

# Example 2: Create another object
p = Person()
print(p.name)

# Example 3: Modify instance attributes
pt = Point()
pt.x, pt.y = 2, 3
print(pt.x, pt.y)

# Example 4: Change an instance attribute
l = Lamp()
l.on = True
print(l.on)

# Example 5: Create object and update attribute
b = Book()
b.title = "Python"
print(b.title)