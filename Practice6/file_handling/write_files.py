# Create and write to a file

with open("sample.txt", "w") as f:
    f.write("Hello, this is a sample file.\n")
    f.write("Python file handling practice.\n")

# Append to file
with open("sample.txt", "a") as f:
    f.write("This line is appended.\n")

print("File written and appended successfully.")