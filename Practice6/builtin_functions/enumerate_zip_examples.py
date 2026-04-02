names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate()
for i, name in enumerate(names):
    print(i, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# sorted()
print("Sorted scores:", sorted(scores))

# type conversion
num_str = "123"
num = int(num_str)
print(type(num), num)