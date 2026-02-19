numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry"]

# Example 1: Multiply by 2
print(list(map(lambda x: x * 2, numbers)))

# Example 2: Square numbers
print(list(map(lambda x: x ** 2, numbers)))

# Example 3: Add 10
print(list(map(lambda x: x + 10, numbers)))

# Example 4: Convert to strings
print(list(map(lambda x: str(x), numbers)))

# Example 5: Uppercase words
print(list(map(lambda s: s.upper(), words)))