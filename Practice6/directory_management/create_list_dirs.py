import os

# Create directory
os.mkdir("test_dir")

# Create nested directories
os.makedirs("parent_dir/child_dir", exist_ok=True)

# List directory contents
print("Files and folders:", os.listdir("."))

# Current directory
print("Current dir:", os.getcwd())

# Remove directory
os.rmdir("test_dir")