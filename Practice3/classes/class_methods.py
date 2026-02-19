class Person:
    # A method that uses an instance attribute
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)


class Dog:
    # A simple method without parameters
    def bark(self):
        print("Woof!")


class Counter:
    # Methods can change object state
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1


class Calc:
    # Methods can return values
    def add(self, a, b):
        return a + b


class Box:
    # A method can compute something using arguments
    def area(self, w, h):
        return w * h


# Example 1
Person("Emil").greet()
# Example 2
Dog().bark()
# Example 3
c = Counter()
c.inc()
c.inc()
print(c.value)
# Example 4
print(Calc().add(2, 3))
# Example 5
print(Box().area(3, 4))