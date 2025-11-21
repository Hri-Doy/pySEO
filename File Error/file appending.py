# file = open('File Error/3.txt', 'a')
# file.writelines('Hello World!\n')
# file.close()

with open('File Error/4.txt', 'a') as file:
    file.writelines('This is a new line five times\n' * 5)

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''