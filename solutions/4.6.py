ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
x = ospf_route.split()
template = f"""
Prefix                {x[0]}
AD/Metric             {x[1].strip('[]')}
Next-Hop              {x[3].strip(',')}
Last update           {x[4].strip(',')}
Outbound Interface    {x[5]}
"""
print(template)