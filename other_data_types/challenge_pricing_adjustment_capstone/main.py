grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)
}

eggs_category, eggs_price, eggs_stock = grocery_inventory["Eggs"]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (eggs_category, eggs_price - 1, eggs_stock)
else:
    print("The price of Eggs is reasonable.")

# Manage Stock
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    # Update the tuple first
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        milk_stock + 20
    )
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.", grocery_inventory["Milk"][2])

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

# Remove Apples based on price
Apples_category, Apples_price, Apples_stock = grocery_inventory["Apples"]
if Apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)

