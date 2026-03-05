import re
import json

# Open the receipt text file and read its content
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Lists to store product names and their prices
products = []
prices = []

# Split the text into separate lines
lines = text.split("\n")

# Iterate through all lines of the receipt
for i in range(len(lines)):
    
    # Look for a line that contains quantity and price pattern (e.g., "2,000 x 154,00")
    match = re.search(r"\d+,\d+\s*x\s*([\d\s]+,\d{2})", lines[i])
    
    if match:
        # Extract the price and convert it to a standard float format
        price = match.group(1).replace(" ", "").replace(",", ".")
        
        # The product name is located in the line above
        product = lines[i-1].strip()
        
        # Add product name and price to lists
        products.append(product)
        prices.append(float(price))

# Calculate the total price of all products
total = round(sum(prices), 2)

# Search for date and time in the receipt
date_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}", text)
date_time = date_match.group() if date_match else "Not found"

# Determine the payment method (Bank card in this receipt)
payment_match = re.search(r"Банковская карта", text)
payment_method = "Card" if payment_match else "Not found"

# Create a dictionary with the extracted receipt information
receipt = {
    "products": products,
    "prices": prices,
    "total": total,
    "date_time": date_time,
    "payment_method": payment_method
}

# Print the result in JSON format
print(json.dumps(receipt, indent=4, ensure_ascii=False))