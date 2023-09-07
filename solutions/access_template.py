from sys import argv
#требует при запуске 2 аргумента
#например: .\source\access_template.py Gi0/7 4
interface = argv[1]
vlan = argv[2]
access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))