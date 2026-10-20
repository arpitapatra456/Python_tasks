d = {}
fobj = open('network.cfg', 'r')
l = fobj.readlines()
fobj.close()
for var in l:
    var = var.strip()
    k,V = var.split('=')
    d[k] = V

for var in d:
    print(f'{var} = {d[var]}')

d['Interface'] = "Eth0"
d['bootproto'] = "dhcp"
d['onboot'] = "no"
d['IPADDR'] = "192.168.1.100"
d['PREFIX'] = "24"
d['DNS2'] = "122.33.44.556"
for var in d:
    print(f'{var} - {d[var]}')

    wobj = open('new_network.cfg', 'w')
    for var in d:
        wobj.write(f'{var} = {d[var]}\n')
    wobj.close() 