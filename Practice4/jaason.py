# This program reads a JSON file and prints formatted interface information
# Import built-in json module to work with JSON files
import json
# Open the JSON file and load its content into a Python dictionary
with open("sample-data.json") as f:
    data = json.load(f)

# Print table header formatting
print("="*100)
print("DN".ljust(55), "Description".ljust(15), "Speed".ljust(10), "MTU")#a string, padding it with a specified character to reach a desired widt
print("-"*100)

# Loop through each interface object inside the "imdata" list
for item in data["imdata"]:
    att=item["l1PhysIf"]["attributes"]# Access nested dictionary: l1PhysIf -> attributes
     # Extract required fields from attributes
    dn=att["dn"]
    des=att["descr"]
    speed=att["speed"]
    mtu=att["mtu"]
    
    # Print formatted row for each interface
    print(dn.ljust(55), des.ljust(15), speed.ljust(10), mtu)