import os

'''
os.mkdir('Another Directory') # Make a directory
os.getcwd() # See the current a Directory
os.listdir() # See the lists of the files
os.chdir('pySEO') # Change the directory
'''
#os.mkdir('Another Directory') # Make a directory
#print(os.getcwd()) # Change a Directory
os.chdir('pySEO')
#print(os.getcwd()) 
# print(os.listdir()) # See the lists of the files

rename = os.rename('1.txt', 'text_file.txt')
print(rename)