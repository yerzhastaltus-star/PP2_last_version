ages = [5, 12, 17, 18, 24, 32]
nums = [1, 2, 3, 4, 5, 6]
words = ["hi", "", "bye", ""]
scores = [40, 55, 90, 20]
names = ["Ann", "Bob", "Christopher"]

# Example 1: Filter adults
print(list(filter(lambda x: x >= 18, ages)))

# Example 2: Filter even numbers
print(list(filter(lambda x: x % 2 == 0, nums)))

# Example 3: Remove empty strings
print(list(filter(lambda s: s != "", words)))

# Example 4: Filter passing scores
print(list(filter(lambda s: s >= 50, scores)))

# Example 5: Filter long names
print(list(filter(lambda n: len(n) > 3, names)))