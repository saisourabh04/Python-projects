# Write a Python program to calculate the discounted price of an item based on its original price.
# Discount Rules:
# If the original price of the item is more than $100, a 10% discount applies.
# If the original price is $100 or less but more than $50, a 5% discount applies.
# If the original price is $50 or less, there's no discount.
# Your program should:
# Ask the user to input the original price of the item.
# Use conditional statements to apply the appropriate discount based on the discount rules.
# Calculate the final price after discount and print it to the user.
discount=0
original_price=float(input('enter the price in $'))
if original_price > 100:
    discount= original_price*0.1
elif original_price <= 100 and original_price >50:
    discount= original_price*0.05
else:
    discount=0
final_price=original_price-discount
print(f'final price after discount ${final_price}')

