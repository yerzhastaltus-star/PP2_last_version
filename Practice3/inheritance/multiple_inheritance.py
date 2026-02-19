class A:
    def a(self):
        return "A"


class B:
    def b(self):
        return "B"


class C(A, B):
    # Inherit from both A and B
    pass


class X:
    def who(self):
        return "X"


class Y:
    def who(self):
        return "Y"


class Z(X, Y):
    # If both parents have the same method name, MRO chooses the first
    pass


# Example 1
c = C()
print(c.a(), c.b())
# Example 2
print(isinstance(c, A), isinstance(c, B))
# Example 3
print(Z().who())
# Example 4
print(Z.__mro__)
# Example 5
print(C.__mro__)