from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() - square numbers
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter() - even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# reduce() - sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)