access_template = {
    "switchport mode access",
    "switchport access vlan {vlans}",
    "switchport nonegotiate",
    
}


print('Введите режим работы интерфейса (access/trunk): ')
mode = input()
print('Введите тип и номер интерфейса: ')
interface = input()
print('Введите номер влан(ов): ')
vlans = input()

print('interface ' + interface + '\n')
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable


interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
