file = open('File Error/1.txt', 'r')
content = file.readlines() 
'''
# read : reads the whole text
# readline : Reads one line at a time
# readlines : 's' Creates a list of lines
# '''
print(content)
file.close()

'''
NB: You must close the file. 
Otherwise, it runs always.
And memory consumtion continues.
'''