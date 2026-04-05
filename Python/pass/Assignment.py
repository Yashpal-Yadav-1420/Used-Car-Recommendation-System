# Python program to calculate discount and final amount

# Input: User's total purchase amount
"""purchase_amount = int(input("Enter your total purchase amount (₹): "))

# Determine the applicable discount rate
if 1000 <= purchase_amount <= 4999:
    discount_rate = 5
elif 5000 <= purchase_amount <= 9999:
    discount_rate = 10
elif 10000 <= purchase_amount <= 49999:
    discount_rate = 15
elif purchase_amount >= 50000:
    discount_rate = 20
else:
    discount_rate = 0  # No discount for amounts below ₹1,000

# Calculate the discount amount and final amount
discount_amount = (discount_rate / 100) * purchase_amount
final_amount = purchase_amount - discount_amount

# Output
print(f"Purchase Amount: ₹{purchase_amount}")
print(f"Applicable Discount Rate: {discount_rate}%")
print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Final Amount After Discount: ₹{final_amount:.2f}")"""

# Python program to compare temperature and wind speed

# Input values from the user
"""temp = float(input("Enter the temperature in Celsius: "))
wind_speed = float(input("Enter the wind speed in km/h: "))

# Check if temperature is equal to wind speed
if temp == wind_speed:
    print("Temperature and wind speed are the same.")
else:
    # Determine which value is greater
    if temp > wind_speed:
        print("Temperature is greater than wind speed.")
        larger = temp
        smaller = wind_speed
    else:
        print("Wind speed is greater than temperature.")
        larger = wind_speed
        smaller = temp

    # Handle division by zero
    if smaller != 0:
        quotient = larger / smaller
        remainder = larger % smaller
        print(f"Quotient when dividing the larger value by the smaller one: {quotient:.2f}")
        print(f"Remainder when dividing the larger value by the smaller one: {remainder:.2f}")
    else:
        print("Division by zero is not possible.")"""





