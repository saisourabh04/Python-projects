#set is another data structure
#we use curly brackets{}
#set's are unindexed and unorderly.


s1={11,21,33,44,55,55,55,56}
s2={9,8,2,11,33,}
# s3=s1.union(s2)
# s3=s1.intersection(s2)
# print(s3)
# s.add(24)
# print(s)
# s.remove(33)
# print(s)
# print(s)
d=s1.difference(s2)
print(d)
print(s1-s2)
print(s1&s2)
print(s1^s2)
print(s1|s2)

l=[1,1,2,2,3,4,5,6,7,7,8,8,9]
print(list(set(l)))
for i in s1:
    print(i)
