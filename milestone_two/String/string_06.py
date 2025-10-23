'''
In string, the usage of:
# find, 
# rfind,
# replace
'''

txt = "Hello, welcome to our world."

print(txt.index('we'))
print(txt.find("we"))
print(txt.find("we3"))
print(txt.rfind('w')) # Counts from right

# string.find(substring, start[option], end[optional])


name = 'Shanta Islam Runy'
print(name.replace('Shanta', 'Santa'))