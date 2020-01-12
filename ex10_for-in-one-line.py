ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

my_flight = [(port1, port2) for port1 in ports for port2 in ports]
print(my_flight)
print(len(my_flight))
print('-' * 80)

my_flight = [(port1, port2) for port1 in ports for port2 in ports if port1 != port2]
print(my_flight)
print(len(my_flight))
print('-' * 80)

my_flight = [(port1, port2) for port1 in ports for port2 in ports if port1 < port2]
print(my_flight)
print(len(my_flight))

