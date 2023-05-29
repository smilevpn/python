import re
#докидывает в строку пробелы до 10 символов
def quantiti_symbols(value):
    return value + ((10 - len(value)) * ' ')

#разделяет ip и маску
def separation_ip(ip_and_mask):
    return (ip_and_mask.split('/'))[0]
def separation_mask(ip_and_mask):
    return (ip_and_mask.split('/'))[1]

#формирует обработанный вывод адреса
def out_ip(ip):
    octets = ip.split('.')
    i = 0
    res_bin, res_oct = '', ''
    while i < len(octets):
        x = int(octets[i])
        res_oct += quantiti_symbols(octets[i])
        res_bin += quantiti_symbols(format(x, '08b'))
        i += 1
    return (res_oct + '\n' + res_bin)

#формирует обработанный вывод маски
def out_mask(mask):
    octets = '255.255.255.0'.split('.')
    res_oct, res_bin = '', ''
    i = 0
    while i < len(octets):
        x = int(octets[i])
        res_oct += quantiti_symbols(octets[i])
        res_bin += quantiti_symbols(format(x, '08b'))
        i += 1
    return ('/' + mask + '\n' + res_oct + '\n' + res_bin)

print(40 * '-' + '\n' + 'Введите ip-адрес по маске x.x.x.x/xx: ')
ip_and_mask = input()
for val in ip_and_mask:
    if re.match(r'([0-9]{3}|[0-9]{2}|[0-9]{1})\.([0-9]{3}|[0-9]{2}|[0-9]{1})\.([0-9]{3}|[0-9]{2}|[0-9]{1})\.([0-9]{3}|[0-9]{2}|[0-9]{1})\/([0-9]{2}|[0-9]{1})', val) == True:
        print('yes')
    else:
        print('Неверное значение')
        quit()
ip = separation_ip(ip_and_mask)
mask = separation_mask(ip_and_mask)

print(40 * '-' + '\n' + 'Network:' + '\n' + out_ip(ip) + '\n\n' + 'Mask:' + '\n' + out_mask(mask) + '\n' + 40 * '-')
