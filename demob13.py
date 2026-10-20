import pprint
empty_dict = {}
limit=0
while limit < 5:
    host01 = input("Enter alias: ")
    host_ip = input("Enter host IP: ")
    empty_dict[host01] = host_ip
    limit += 1
for var in empty_dict:
    print(f'{var} - {empty_dict[var]}')
    print('')
    k = input ('enter alias name')
    if k in empty_dict:
        print(f'sorry input host{k} already exists.')
        print('enter different hostname')
        continue
    v = input('enter host IP')
    empty_dict[k] = v
    count += 1
    print('hostname\t ipaddress')
    if alias_name in empty_dict:
        empty_dict[host01] = '127.0.0.1'
        print(f"Found: Alias: {alias_name}, IP: {host_ip}")
        
    else:
        empty_dict[host01] = '127..0.0.1'
        print("Alias not found.")
    pprint.pprint(empty_dict)