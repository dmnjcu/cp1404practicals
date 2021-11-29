"""
CP1404/CP5632 - Practical
Shop calculator program to determine total price after discount
"""

total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount

print(f"Total price for {number} items is ${total:.2f}")
