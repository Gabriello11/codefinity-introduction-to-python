produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

print("Inventory list")
#
groceries = [produce, dairy]
for section in groceries:        # outer: section is one sublist at a time
    for item in section:         # inner: item is each element in that sublist
        print("Item name:", item)

    
    

