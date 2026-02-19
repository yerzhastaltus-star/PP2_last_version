class Person:
    # __init__ runs when you create the object
    def __init__(self, name):
        self.name = name


class Student:
    # __init__ can take multiple values
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car:
    # Store brand in the object
    def __init__(self, brand):
        self.brand = brand


class Pair:
    # Store two values
    def __init__(self, a, b):
        self.a = a
        self.b = b


class BankAccount:
    # Default argument for balance
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


# Example 1
print(Person("Emil").name)
# Example 2
s = Student("Ann", 18)
print(s.name, s.age)
# Example 3
print(Car("BMW").brand)
# Example 4
p = Pair(1, 2)
print(p.a, p.b)
# Example 5
acc = BankAccount("Ernur", 100)
print(acc.owner, acc.balance)