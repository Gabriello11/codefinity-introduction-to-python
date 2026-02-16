# 1. Initialize the lists
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# 2. Combine into deli_dept
deli_dept = [meat, cheese, condiment]

# 3. Print initial state
print("Initial Deli List:", deli_dept)

# 4. Restock Ham if quantity < 100
if meat[0] == "Ham" and meat[2] < 100:
    meat[2] = 100

# 5. Add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# 6. Remove the condiment list
deli_dept.remove(condiment)

# 7. Sort by the item name (first element)
deli_dept.sort(key=lambda item: item[0])

# 8. Print updated state
print("Updated Deli List:", deli_dept)