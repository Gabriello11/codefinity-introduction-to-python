prices = [29.99, 45.50, 12.75, 38.20]

for Index in range(len(prices)):
    # 1) choose discount per index
    if Index == 0:
        discount_factor = 0.10
    elif Index == 1:
        discount_factor = 0.20
    elif Index == 2:
        discount_factor = 0.15
    else:
        discount_factor = 0.05

    # 2) apply discount
    prices[Index] -= prices[Index] * discount_factor

    # 3) print result
    print(f"New price of item {Index + 1}: ${prices[Index]:.2f}")




    