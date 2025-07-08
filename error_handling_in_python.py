x=3
if x % 2==0:
    print('even number')
else:
    print('odd number')
try:
    names=['bill','mike','jim','jill','kim']
    print(names[4])
except IndexError as error:
    print('give in the range only',error)
else:
    print('program ran successfully')
finally:
    print('program is over')


student={'first_name':'kim','last_name':'lop'}
try:
    print(student['name'])  #key error
except KeyError as err:
    print('pls check the key',err)
else:
    print('program ran successfully')
finally:
    print('over bye bye')


# age=''
# new_age=int(age)------------value error
# print(new_age)
#
# with open('xyz.txt') as file:---------file not found error
#     print(file.read())
#
# data='2'+5--------Type error
# print(data)

print(student.items())
# print(names.items())-------attribute error

