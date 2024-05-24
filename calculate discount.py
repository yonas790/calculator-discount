price = float(input("Price: "))
discount_percent = float(input("Discount percent(e.g., 0.25): "))
def calculate_discount(price, discount_percent): 
   if discount_percent > 0.2:
      final_price = price - (price * discount_percent)
      return final_price
   else: 
      return price
print(calculate_discount(price, discount_percent))