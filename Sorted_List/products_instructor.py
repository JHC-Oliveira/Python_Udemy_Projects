import copy

# copy, sorted, products.sort
# Exercises
# Increase the prices of the following products by 10%
# Generate new_products using deep copy
products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

new_products = [
    {**p, 'price': round(p['price'] * 1.1, 2)}
    for p in copy.deepcopy(products)
]

# Sort products by name in descending order (from highest to lowest)
# Generate products_sorted_by_name using deep copy
products_sorted_by_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['name'],
    reverse=True
)

# Sort products by price in ascending order (from lowest to highest)
# Generate products_sorted_by_price using deep copy
products_sorted_by_price = sorted(
    copy.deepcopy(products),
    key=lambda p: p['price']
)

# FINAL

print(*products, sep='\n')
print()
print(*new_products, sep='\n')
print()
print(*products_sorted_by_name, sep='\n')
print()
print(*products_sorted_by_price, sep='\n')
