grocery_inventory = {
    "Milk": (113, "Dairy"), "Eggs": (116, "Dairy"),"Bread": (117, "Bakery") ,"Apples": (141, "Produce")
}

#Bread Details
bread_details = grocery_inventory["Bread"]
print("Details of Bread:", bread_details)

#Add A New Item
grocery_inventory.update({"Cookies":(143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)

#Remove the item "Eggs" from the dictionary
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", (grocery_inventory))
