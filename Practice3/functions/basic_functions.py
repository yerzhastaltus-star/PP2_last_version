# Example 1: Simple function
def hello():
    print("Hello")


# Example 2: Function with parameters
def add(a, b):
    return a + b


# Example 3: Function that returns a value
def square(x):
    return x * x


# Example 4: Default parameter value
def greet(name="World"):
    print("Hello", name)


# Example 5: Function returning boolean
def is_even(n):
    return n % 2 == 0


hello()
print(add(2, 3))
print(square(4))
greet()
print(is_even(10))