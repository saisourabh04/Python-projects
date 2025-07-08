#in tuple its almost like a list but its immutable. It uses ()

t=('red','rose','tom')
print(t)
print(type(t))
print(t[1])
# t[1]='tulip'
for x in t:
    print(x)
print(t.count('rose'))
print(t.index('rose'))