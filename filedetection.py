import os
path = '/Users/loki/Desktop/python/filedetection.py'
if os.path.exists(path):
    print('that location exist')
    if os.path.isfile(path):
        print('that is a file')
    elif os.path.isdir(path):
        print('it is adirctory')

    
else:
    print('that location doensnt exist')

text = 'Yoooooooooooooo\n this this is the new one have a good one'
try:
 with open('test.txt','a') as file:
     print(file.write(text))
 print(file.closed)

except FileNotFoundError:
    print('that file was not found')


