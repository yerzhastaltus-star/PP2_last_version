class Person:
    def __init__(self, fname):
        self.fname = fname


class Student(Person):
    # Use super() to call parent __init__
    def __init__(self, fname):
        super().__init__(fname)


class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20


class Animal:
    def speak(self):
        return "sound"


class Dog(Animal):
    def speak(self):
        return super().speak() + " woof"


# Example 1
print(Student("Emil").fname)
# Example 2
b = B()
print(b.x, b.y)
# Example 3
print(Dog().speak())
# Example 4
print(isinstance(b, A))
# Example 5
print(isinstance(Student("Ann"), Person))