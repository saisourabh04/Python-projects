# 1. View shopping cart
# 2. Add item to cart
# 3. Remove item from cart
# 4. Show total items in cart
# 5. Search an item in cart
# 6. Show total cost
# 7. Quit
#
# Enter your choice: 2
#
# Enter the item you wish to add: Apple
# Enter the price of the item: 50
#
# 1. View shopping cart
# 2. Add item to cart
# 3. Remove item from cart
# 4. Show total items in cart
# 5. Search an item in cart
# 6. Show total cost
# 7. Quit
#
# Enter your choice: 1
#
# Your shopping cart:
# Item No.   Item                 Price
# ----------------------------------------
# 1          Apple                50.00

menu="""welcome to shopping
1. View shopping cart
2. Add item to cart
3. Remove item from cart
4. Show total items in cart
5. Search an item in cart
6. Show total cost
7. Quit

Enter your choice:
"""
choice= None
shopping_cart=[]
price_list=[]
while choice != 7:
    choice = int(input(menu))
    if choice==1:
        print("Your shopping Cart:")
        print(f"{'item no.':<10} {'Item':<20} {'Price':<10}")
        print("-"*40)
        i=0
        for item in shopping_cart:
            print(f"{i+1:<10} {item:<20} {price_list[i]:<10}")
            i+=1
    elif choice==2:
        item=input("Enter Item:")
        quantity=int(input("Quantity:"))
        item_qty=f"{item}-{quantity} no.s"
        shopping_cart.append(item_qty)
        price=float(input("Price:"))
        price_list.append(price)
        print(f"{item} is added to cart")
    elif choice==3:
        item_remove=input(("Enter Item:"))
        for item in shopping_cart:
            if item_remove in item:
                idx=shopping_cart.index(item)
                shopping_cart.remove(item)
                price_list.pop(idx)
                print('your item was removed')
    elif choice==4:
        total_items=len(shopping_cart)
        print(f'you have a total of {total_items} items')
    elif choice==5:
        search_item=input("enter to search item in cart:")
        for item in shopping_cart:
            if search_item in item:
                print(f'{search_item} is in the cart')
                break
        else:
            print(f'{search_item} is not in the list')
    elif choice==6:
        total_cost=sum(price_list)
        print(f'the total cost is {total_cost} dollars')






