# Input
total = int(input("Total Items: "))
per_page = int(input("Items Per Page: "))
page = int(input("Page Number: "))

# Create list
items = list(range(1, total + 1))

# Find start and end index
start = (page - 1) * per_page
end = start + per_page

# Show data of that page
print(items[start:end])