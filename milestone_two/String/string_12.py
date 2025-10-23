'''
String Exercise: Converting String to URI
# Write a Python function to convert string to URL
# Output = santa-islam-runy
'''
str1 = "Santa Islam Runy"

'''
convert into lower case
replace blank space with dash
convert it to function
'''

# str1 = "Santa Islam Runy"
# lower_case = str1.lower()
# url = lower_case.replace(" ", "-")
# print(url)

# name = "Santa Islam Runy"

def urlify(string):
    lower_case = string.lower()
    url = lower_case.replace(" ", "")
    return url

user_input = urlify(input("Enter your name: ").strip())
web_url = f'https://www.{user_input}.com/'
print(web_url)