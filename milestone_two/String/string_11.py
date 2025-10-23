'''
In string, the usage of:
# zfill
# format_map
'''

person = {
    "name" : "Runy",
    "age" : 20
}
print('My name is {name} and age is {age}'.format_map(person))

'''
The usage of Zfill
It is used to add extra 0 and create a format like calender
'''

num1 = "2"
print(num1.zfill(5))


