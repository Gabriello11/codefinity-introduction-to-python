# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1 = items[:9]        # "Bubblegum"
candy2 = items[11:20]# "Chocolate"

dry_goods = items[22:]    # "Pasta"
category1 = categories[:11]    # "Candy Aisle"
category2 = categories[13:]

#prices
Bubblegum_price = "$1.50"
Chocolate_price = "$2.00"
Pasta_price = "$5.40"

print(" We Have " + candy1 + " for " + Bubblegum_price + " in the " + category1)
print(f"We have {candy1} for {Bubblegum_price} in the {category1}")

print(" We Have " + candy2 + " for " + Chocolate_price + " in the " + category1)
print(f"We have {candy2} for {Chocolate_price} in the {category1}")

print(" We Have " + dry_goods + " for " + Pasta_price + " in the " + category2)
print(f"We have {dry_goods} for {Pasta_price} in the {category2}")