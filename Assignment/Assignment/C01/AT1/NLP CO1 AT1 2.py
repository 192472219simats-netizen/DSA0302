import re

products = [
    "Apple iPhone 15",
    "Apple Watch",
    "Samsung Galaxy S24",
    "Samsung Charger",
    "Dell Laptop",
    "HP Laptop",
    "Wireless Mouse",
    "Bluetooth Speaker",
    "Gaming Keyboard",
    "Python Programming Book"
]

print("Available Products")

for p in products:
    print("-", p)

search = input("\nEnter search keyword: ")

# Exact Search
exact = [p for p in products if re.fullmatch(re.escape(search), p, re.IGNORECASE)]

# Prefix Search
prefix = [p for p in products if re.match(re.escape(search), p, re.IGNORECASE)]

# Suffix Search
suffix = [p for p in products if re.search(re.escape(search) + r"$", p, re.IGNORECASE)]

# Partial Search
partial = [p for p in products if re.search(re.escape(search), p, re.IGNORECASE)]

print("\n========== Search Results ==========")

print("\nExact Match")
print(exact)

print("\nPrefix Match")
print(prefix)

print("\nSuffix Match")
print(suffix)

print("\nPartial Match")
print(partial)

print("\n========== Report ==========")
print("Exact Matches :", len(exact))
print("Prefix Matches :", len(prefix))
print("Suffix Matches :", len(suffix))
print("Partial Matches :", len(partial))
