products = [
    {"name": "AC 1", "price": 25000, "status": "In Stock"},
    {"name": "AC 2", "price": 35000, "status": "Pre Order"},
    {"name": "AC 3", "price": 45000, "status": "In Stock"},
    {"name": "AC 4", "price": 60000, "status": "Up Coming"}
]

min_price = int(input("Minimum Price: "))
max_price = int(input("Maximum Price: "))
status = input("Availability: ")

for product in products:    
    if (min_price <= product["price"] <= max_price) and (product["status"] == status):

        print( product["name"])
        print( product["price"])
        print("Status:", product["status"])
        