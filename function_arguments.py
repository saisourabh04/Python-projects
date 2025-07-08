#positional argument.
def rect_area(l,b):
    return f"length:{l} width:{b}=area:{l*b}"
print(rect_area(25,8))

#keyword argument
print(rect_area(b=8,l=25))

#arbitrary positional arguments.
def find_sum(*nums):
    return sum(nums)
print(find_sum(3,7,9,8))

#arbitrary keyword argument

def print_info(**info):
    print(info)
print_info(f_n='sai',l_n='sourabh',age=65,sex='m')

#default argument
def reg_emp(f_n,l_n,age,sex,country='usa'):
    print(f'person {f_n}{l_n} age: {age} country: {country} sex: {sex}')
reg_emp('sai','sourabh',34,'m','uk')

