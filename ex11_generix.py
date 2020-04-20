ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO']

my_flight1 = ((start,stop) for start in ports for stop in ports)

my_flight2 = ((start,stop) for start in ports for stop in ports if start != stop)

my_flight3 = [(port1, port2) for port1 in ports for port2 in ports if port1 < port2]

counter1 = 0
counter2 = 0
counter3 = 0

for i in my_flight1:
    counter1 += 1

for i in my_flight2:
    counter2 += 1

for i in my_flight3:
    counter3 += 1

print(counter1)
print(counter2)
print(counter3)