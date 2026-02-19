class Person:
    # Parent class with __init__
    def __init__(self, fname):
        self.fname = fname


class Student(Person):
    # Child class inherits everything from Person
    pass


class Animal:
    def sound(self):
        return "..."


class Dog(Animal):
    # Inherits sound() from Animal
    pass


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def honk(self):
        return "Beep!"


# Example 1
s = Student("Emil")
print(s.fname)
# Example 2
print(Dog().sound())
# Example 3
c = Car("Ford")
print(c.brand, c.honk())
# Example 4
print(isinstance(s, Person))
# Example 5
print(isinstance(c, Vehicle))