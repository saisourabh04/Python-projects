student_info={'name':'akash' ,'age': 45, 'height': 5.9}
print(student_info)
print(type(student_info))

print(student_info.get('heights',5.4))
student_info['name']='firoz'
print(student_info)
student_info['weight']= 56
print(student_info)

student_info.update({'phone': 45679 , 'email': 'abcd@gmail.com'})
student_info.update({'phone': 45679 , 'email': 'abcdc@gmail.com'})
print(student_info)


print(student_info.pop('name'))
print(student_info.keys())
print(student_info.values())
print(student_info.items())

for x in student_info.items():                  #for looping in dict
    print(f"{x[0]}: {x[1]}")


