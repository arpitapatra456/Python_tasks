empty_L = []
print(len(empty_L))
limit = 0
while(limit < 5):
    d_name = input("Enter a name: ")
    empty_L.append(d_name)
    limit += 1
print(len(empty_L))
for name in empty_L:
    print(name)
dev = input("Enter a device name: ")
if dev in empty_L:
    print(f"{dev} is found at index {empty_L.index(dev)}")
else:
    print(f"{dev} is not found in the list")
    empty_L.append(dev)
    print(f"{dev} has been added to the list")
print((empty_L))