'''
In string, the usage of:
# center
# ljust
# rjust
# expandtabs
# join 
# slicing
'''

txt_one = 'Santa Islam Runy'
txt_two = 'Santa'
txt_three = 'Santa lives in\t Vakral'
txt_four = 'my name is Santa'

print(len(txt_one)) # Total characters with spaces

# Now I want to print it with 50 characters
# If I want nothing, just keep it blank
# If you want something, add that, I added # here
print(txt_one.center(20, "#")) 
# The total len is 16 and added four # in both side which is 20 now.

# Only for left use ljust
print(txt_one.ljust(20, "y"))

# Only for right use rjust
print(txt_one.rjust(20, "S"))

'''
In string, the usage of:
# string.expandtabs()
- This is used to customize the tabs limit
- By default, the tab is 8 character. 
- Now I can make it to anything.
'''

txt_three = 'Santa lives in\t Vakral'
print(txt_three.expandtabs(20))

'''
In string, the usage of:
# join 
# Join the opposite of split
'''

name = "My name is Runy"
print(name.split())

her = ['My', 'name', 'is', 'Runy']
print(" ".join(her))

# here " ".join(variable)
# The brackets needs the variable to be inside


'''
In string, the usage of:
# slicing
'''

poem = "She walks in beauty by Lord Byron"
print(poem[2])
print(poem[:10])
print(poem[10:])
print(poem[5:11])