numbers = [1,2,3,4,5,6,7,8,9]
try:
    print(numbers[10])
except:
    print('You are wrong!')
    
num = [1,2,3,4,5,6,7,8,9]
try:
    print(num[11])
except:
    pass
print('The upper ones didn\'t work')


# User useage cases
try:
    numb = int(input('Enter a number: '))
    print(numb, 'Good!')
except:
    print('You din\'t input a number')