'''
In string, the usage of:
# startwith
# endswith
# index
# rindex
'''
str1 = "Python is awesome, isn't it? I love python"

print(str1.startswith('Python'))
print(str1.startswith('P'))
print(str1.endswith('python'))
print(str1.endswith('n'))
print(str1.index("is", 2))
print(str1.rindex("is"))


# String index
# string.index(substing, start[optional], end[optional])
# string.rindex(substing, start[optional], end[optional]) ---- Start from the right side.