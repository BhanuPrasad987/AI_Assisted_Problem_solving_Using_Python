#simplify and refactor the below python code snippet for readability.
'''def discount(price, category):
    if category == "student":
        if price > 1000:
            return price * 0.9
        else:
            return price * 0.95
    else:
        if price > 2000:
            return price * 0.85
        else:
            return price'''
def discount(price, category):
    if category == "student":
        discount_rate = 0.9 if price > 1000 else 0.95
    else:
        discount_rate = 0.85 if price > 2000 else 1.0
    return price * discount_rate

# Example usage:
final_price = discount(1500, "student")
print(final_price)  # Output: 1350.0

