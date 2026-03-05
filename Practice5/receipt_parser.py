import re
import json

# read text file
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# find products and prices
items = re.findall(r"([A-Za-z ]+)\s+(\d+\.\d{2})", text)

products = []
prices = []

for name, price in items:
    products.append(name)
    prices.append(float(price))

# calculate total
total = round(sum(prices), 2)

# find date and time
date_match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", text)
date_time = date_match.group() if date_match else "Not found"

# find payment method
payment_match = re.search(r"Payment Method: (\w+)", text)
payment_method = payment_match.group(1) if payment_match else "Not found"

# create dictionary
receipt = {
    "products": products,
    "prices": prices,
    "total": total,
    "date_time": date_time,
    "payment_method": payment_method
}

# print json
print(json.dumps(receipt, indent=4))