import copy  # Import copy module to make deep (full) copies of lists/dictionaries

# Original list of products
products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

# Function to print each product's name and price
def show_product(product_list):
    for item in product_list:
        print(f"Name: {item['name']}, Price: {item['price']:.2f}")

# -------------------------
# 1. Increase prices by 10%
# -------------------------

# Make a deep copy so the original list remains unchanged
new_products = copy.deepcopy(products)

# Add 10% to each product's price
new_products = [
    {**item, 'price': item['price'] * 1.1}
    for item in new_products
]

print('10% PRICE INCREASE')
show_product(new_products)
print()

# -----------------------------------------------
# 2. Sort products by name in descending order (Z to A)
# -----------------------------------------------

# Deep copy again to keep original data safe
products_sorted_by_name = copy.deepcopy(products)

# Sort the list by the 'name' key, in reverse alphabetical order
products_sorted_by_name.sort(key=lambda item: item['name'], reverse=True)

print('SORTED BY NAME (DESCENDING)')
show_product(products_sorted_by_name)
print()

# -----------------------------------------------
# 3. Sort products by price in ascending order (Low to High)
# -----------------------------------------------

# Deep copy to preserve original list
products_sorted_by_price = copy.deepcopy(products)

# Sort by the 'price' key, smallest to largest
products_sorted_by_price.sort(key=lambda item: item['price'])

print('SORTED BY PRICE (ASCENDING)')
show_product(products_sorted_by_price)
