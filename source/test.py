import re
result = re.match(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}\/[0-9]{2}', '.111.111.111/24')
print(type(result))