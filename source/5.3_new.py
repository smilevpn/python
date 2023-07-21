print('Введите режим работы интерфейса (access/trunk): ')
mode = input()
print('Введите тип и номер интерфейса: ')
interface = input()
print('Введите номер влан(ов): ')
vlans = input()

access_template = [
    "switchport mode access",
    f"switchport access vlan {vlans}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    f"switchport trunk allowed vlan {vlans}",
]

print('interface ', interface)
print()