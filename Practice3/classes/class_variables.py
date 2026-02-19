class A:
    # Class variable shared by all instances
    x = 10


class Car:
    # Class variable shared by all cars
    wheels = 4


class User:
    # Shared default role
    role = "guest"


class Counter:
    # Class variable used to count instances
    count = 0

    def __init__(self):
        Counter.count += 1


class Flag:
    # Shared boolean value
    value = False


# Example 1
print(A.x)
# Example 2
print(Car.wheels)
# Example 3
u1 = User()
u2 = User()
print(u1.role, u2.role)
# Example 4
Counter()
Counter()
Counter()
print(Counter.count)
# Example 5
print(Flag.value)