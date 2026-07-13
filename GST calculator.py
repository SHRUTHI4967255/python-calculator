print("=" * 45)
print("         GST CALCULATOR")
print("=" * 45)

product = input("Enter Product Name : ")

price = float(input("Enter Product Price (₹): "))

gst = float(input("Enter GST Percentage (%): "))

gst_amount = (price * gst) / 100

final_price = price + gst_amount

print()

print("=" * 45)
print("             BILL")
print("=" * 45)

print("Product Name      :", product)

print("Original Price    : ₹", price)

print("GST Percentage    :", gst, "%")

print("GST Amount        : ₹", gst_amount)

print("Final Price       : ₹", final_price)

print("=" * 45)

print("Thank You!")
