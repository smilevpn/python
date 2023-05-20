import sys
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
res = nat.replace('FastEthernet0/1', 'GigabitEthernet')
print(res)