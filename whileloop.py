#write a program which checks given number is prime number or not

num=int(input("enter number:"))
i=1
count=0
while i<=num:
    if num % i == 0:
        count+=1
    i+=1
if count==2:
    print(f"number{num} is prime ")
else:
    print(f"number{num} is not prime ")
