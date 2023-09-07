print('Введите режим работы интерфейса (access/trunk): ')
mode = input()
print('Введите тип и номер интерфейса: ')
interface = input()
print('Введите номер влан(ов): ')
vlans = input()
dict = {
    "access": {
        "switchport mode access",
        f"switchport access vlan {vlans}",
        "switchport nonegotiate",
        "spanning-three portfast",
        "spanning-three bpduguard enable", 
        },
    "trunk": {
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        f"switchport trunk allowed vlan {vlans}",
        }
    }


print('interface ' + interface + '\n')
print(dict[mode])
