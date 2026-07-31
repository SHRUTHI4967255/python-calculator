print("=" * 45)
print("       SMART DISCOUNT CALCULATOR       ")
print("=" * 45)

product = input("Enter Product Name : ")

actual_price = float(input("Enter Actual Price (₹): "))

discount = float(input("Enter Discount Percentage (%): "))

discount_amount = (actual_price * discount) / 100

final_price = actual_price - discount_amount

print("\n========== BILL ==========")

print("Product Name      :", product)

print("Actual Price      : ₹", actual_price)

print("Discount          :", discount, "%")

print("You Saved         : ₹", discount_amount)

print("Final Price       : ₹", final_price)

print("=" * 45)

print("Happy Shopping! 😊")
