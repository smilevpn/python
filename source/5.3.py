# def sum_interfaces():
#     sum_int = ''
#     for key in dict.keys():
#         sum_int += key + ' '
#     return sum_int[:-1]

dict = {
'access':
    "switchport mode access\n"
    "switchport access vlan {vlans}\n"
    "switchport nonegotiate\n"
    "spanning-three portfast\n"
    "spanning-three bpduguard enable\n",
'trunk':
    "switchport trunk encapsulation dot1q\n"
    "switchport mode trunk\n"
    "switchport trunk allowed vlan {vlans}\n"
}


print('Введите режим работы интерфейса (access/trunk): ')
mode = input()
print('Введите тип и номер интерфейса: ')
interface = input()
print('Введите номер влан(ов): ')
vlans = input()

print('interface ' + interface + '\n')
print(dict[mode])
