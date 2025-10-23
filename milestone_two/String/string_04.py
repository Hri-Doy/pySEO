# 'Count, len usage

# Count the length

str1 = "Python is awesome, isn't it?"
print('The total character count is', len(str1))

# Count Method

substring = 'awesome'
print(str1.count(substring))

substring2 = 'i'
print(str1.count(substring2, 8, 20))

# sting.count(substring) ------- Return total count
# sting.count(substring, start, end) ------- Return total count between start and end
