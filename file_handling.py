#reading txt file
# f=open('abc.txt')
# print(f.read())
# f.close()
with open('abc.txt') as file:
    text=file.read()
    #text=file.readlines()[0]
print(len(text.split(' ')))

#writing text file
with open('abc.txt',mode='a') as file:
    file.write('hello from py files')

    