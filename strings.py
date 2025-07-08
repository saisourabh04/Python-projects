city = '   california     '
print(type(city))
a=5
print(type(a))
print(city[4:7])

print(city.upper())
print(city.lower())
print(city.capitalize())
print(city.find('o'))

print(city.strip())



text='poorer,richer,tommmmmy'
words=text.split(',')
print(words)
words_str=''.join(words)
print(words_str)