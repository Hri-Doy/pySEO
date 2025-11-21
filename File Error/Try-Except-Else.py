try:
    number = int(input('Enter a positive number: '))
    if number < 0:
        raise ValueError('The number is not positive.')
except ValueError as ve:
    print('Error', ve)
else:
    print('You Entered: ', number)
finally: # Finally Always runs
    print('The program ends here.')    
