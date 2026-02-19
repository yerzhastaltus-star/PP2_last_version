nums = [5, 2, 9, 1, 7]
words = ["banana", "pie", "apple", "cherry"]

# Example 1: Sort numbers ascending
print(sorted(nums))

# Example 2: Sort numbers descending
print(sorted(nums, reverse=True))

# Example 3: Sort by remainder when divided by 2
print(sorted(nums, key=lambda x: x % 2))

# Example 4: Sort words alphabetically
print(sorted(words))

# Example 5: Sort words by length
print(sorted(words, key=lambda s: len(s)))
