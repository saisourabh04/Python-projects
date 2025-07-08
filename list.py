#list is a data structure , uses [] bracket, is mutable which means items can be modified.
#

shopping_list=['tomato','potato','dal','paneer']
print(type(shopping_list))
print(shopping_list[0:3])
print(shopping_list[-2])

# How to add an item to a list
print (shopping_list.append('roti'))

shopping_list.insert(2,'rice')


shopping_list.extend(['sweets','curd','sabji'])


# how to remove items from list
shopping_list.remove('curd')


print (shopping_list.pop(2))
print(shopping_list)
