command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
cell1 = set((command1.split()[-1]).split(','))
cell2 = set((command2.split()[-1]).split(','))
result = cell1.intersection(cell2)
print(result)