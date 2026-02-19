class Parent:
    def msg(self):
        return "parent"


class Child(Parent):
    # Override the parent method
    def msg(self):
        return "child"


class Base:
    def hello(self):
        return "Hello"


class Extended(Base):
    # Override and also call the parent method
    def hello(self):
        return super().hello() + " from Extended"


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, s):
        self.s = s

    # Override area()
    def area(self):
        return self.s * self.s


# Example 1
print(Child().msg())
# Example 2
print(Extended().hello())
# Example 3
print(Square(4).area())
# Example 4
print(Parent().msg())
# Example 5
print(isinstance(Square(2), Shape))