city_data=[]
no=int(input('enter number of cities: '))
for i in range(no):
    name=input('enter city name :')
    temp=float(input('enter the temp :'))
    t=(name,temp)
    city_data.append(t)
max_city=None
max_temp=city_data[0][1]
for t in city_data:
    city,temp=t
    if temp>max_temp:
        max_temp=temp
        max_city=city
print(f'the{max_city} has maximum temp {max_temp}')