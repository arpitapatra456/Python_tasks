fobj = open('C:\\Users\\arpatra\\emp.csv', 'r')
l = fobj.readlines()
fobj.close()
wobj = open('s1.csv', 'w')
for var in l:
    if 'sales' in var:
        wobj.write(var)
wobj.close()