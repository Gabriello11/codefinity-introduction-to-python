vegetables = ["tomatoes", "potatoes", "onions"]
print("Vegetables:", vegetables)

if "onions" in vegetables:
    vegetables.remove("onions")

if "carrots" not in vegetables:
    vegetables.append("carrots")
print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")

vegetables.sort()
print("Onions are nolonger in the list.")
print("Cucumbers are already in the list.")
print("Carrots are already in the list.")

print("Updated Vegetable Inventory:", vegetables)


