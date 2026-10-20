import time
fobj = open('pin_hostory.log', 'r')
pin = 1234
count = 0
while(count < 3):
    count += 1
    p = input("Enter your PIN: ")
    if(int(p) == pin):
        fobj.write(f'success pin is matched - {count}')
        fobj.write(f'pin entry date/time is {time.ctime()}\n    ')
        print(f'success - pi is matched - {count}')
        break
    else:
        fobj.write(f'failed - user input pin {p} is not matched')
        fobj.write(f'pin entry date/time is {time.ctime()}\n    ')
if(int(p) != pin):
    print('sorry your pin is blocked')
    fobj.write(f'sorry your pin is blocked - blocked time is : {time.ctime()}\n    ')

fobj.close()