def sum_interfaces():
    sum_int = ''
    for key in london_co.keys():
        sum_int += key + ' '
    return sum_int[:-1]
def sum_parameters():
    sum_par = ''
    for key in london_co[interface].keys():
        sum_par += key + ' '
    return sum_par[:-1]

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

interface = input(f'Введите имя сетевого интерфейса ({sum_interfaces()}) : ')
parameter = input(f'Введите имя конкретного параметра ({sum_parameters()}) : ')
print((london_co[interface])[parameter])