emp = ['101,raj,sales,pune,1000',
       '102,anu,marketing,mumbai,2000',
       '103,vikas,hr,delhi,1500',
       '104,sita,finance,chennai,2500',
       '105,ram,it,bangalore,3000']
for e in emp:
    id,name,department,workplace,salary = e.split(',')
    print(e)
    print("emp name in title case:", name.title())
    print("emp work place in upper case:", workplace.upper())
    sum = 0
    sum = sum + int(salary  )
    print("total emp cost:", sum)
