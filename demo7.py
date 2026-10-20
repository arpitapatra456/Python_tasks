pin_number = 1234
count = 0
while(count >= 3):
    pinNumber = int(input("Enter the pin number: "))
    count += 1
    if pinNumber == pin_number:
        print("Access granted.")
        break
if(pin_number != pinNumber):
    print("sorry pin is blocked")