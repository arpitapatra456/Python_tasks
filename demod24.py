print(list(map(lambda a:a,open('C:\\Users\\arpatra\\emp.csv', 'r').readlines())))

print(list(map(lambda var: int(var.split(',')[-1]), filter(lambda var: 'sales' in var, open('C:/Users/Admin/Documents/pytrain/emp.csv', 'r').readlines()))))