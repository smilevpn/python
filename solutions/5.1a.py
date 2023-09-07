london_co = {
"r1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.1"
},
"r2": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.2"
},
"sw1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "3850",
"ios": "3.6.XE",
"ip": "10.255.0.101",
"vlans": "10,20,30",
"routing": True
}
}

interface = input('Введите имя сетевого интерфейса r1|r2|sw1: ')
parameter = input('Введите имя конкретного параметра location|vendor|model|ios|ip|vlans|routing: ')
print((london_co[interface])[parameter])