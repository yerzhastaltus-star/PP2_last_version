import shutil
import os

# Create directory
os.makedirs("move_folder", exist_ok=True)

# Move file
shutil.move("sample.txt", "move_folder/sample.txt")

# Copy back
shutil.copy("move_folder/sample.txt", "sample_restored.txt")

print("File moved and copied.")