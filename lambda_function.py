from functools import reduce

#filter
fun=lambda x:x**3
print(fun(3))

nums=[1,2,3,4]
x=list(filter(lambda x:x>3,nums))
print(x)

#conventional approach without lambda,map functions

x=[]
for num in nums:
    if num>3:
        x.append(num)
print(x)
#map
new_nums=list(map(lambda x:x**2,nums))
print(new_nums)

words=['milk','money','mango','tea']
new_words=list(map(lambda x:x.upper(),words))
print(new_words)

#conventional approach without lambda,map functions
new_words=[]
for word in words:
    new_words.append(word.upper())
print(new_words)


#reduce
s=reduce(lambda x,a:x+a,nums)
print(s)