num=int(input('enter a number whose factorial you wan to find: '))
factorial=1
for x in range(1,num+1):
    factorial *= x
print(f'factorial of {num}:{factorial}')
