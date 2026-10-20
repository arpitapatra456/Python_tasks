file =open('emp.csv' ,'r')
data = file.read()
fobj = open('C:\\users\\admin\\documents\\pytrain\\emp.csv', 'w')
fobj.write(data)
print('File emp.csv contents')
print(data)
print(f'total characters: {len(data)}')
fobj = open('C:\\users\\admin\\documents\\pytrain\\emp.csv', 'r')
l = fobj.readlines()
fobj.close()
print(f'total number of lines: {len(l)}')
for var in l:
    print(var.strip())
    