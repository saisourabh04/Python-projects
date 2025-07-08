num_1=int(input('enter the first_number: '))
num_2=int(input('enter the second_number: '))
operator=input('enter the operation(+,-,*,/,//,%,**):')
if operator=='+':
    result=(num_1 + num_2)
elif operator== '-':
    result=(num_1 - num_2)
elif operator== '*':
    result=(num_1 * num_2)
elif operator== '**':
    result=(num_1 ** num_2)
elif operator== '/':
    result=(num_1 / num_2)
elif operator== '//':
    result=(num_1 // num_2)
elif operator== '%':
    result=(num_1 % num_2)

print(f'{num_1} {operator} {num_2} = {result}')



