from network_masks import dict_mask
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
def out_ip(ip, mask):
    octets_mask = dict_mask[mask].split('.')
    octets = ip.split('.')
    i = 0
    res_bin, res_oct = '', ''
    while i < len(octets):
        if (format(int(octets_mask[i]), '08b')) != '11111111':
            octets[i] = octets_mask[i]
        res_oct += quantiti_symbols(octets[i])
        res_bin += quantiti_symbols(format(int(octets[i]), '08b'))
        i += 1
    return (res_oct + '\n' + res_bin)

#формирует обработанный вывод маски
def out_mask(mask):
    octets = dict_mask[mask].split('.')
    res_oct, res_bin = '', ''
    i = 0
    while i < len(octets):
        x = int(octets[i])
        res_oct += quantiti_symbols(octets[i])
        res_bin += quantiti_symbols(format(x, '08b'))
        i += 1
    return ('/' + mask + '\n' + res_oct + '\n' + res_bin)

#считываем ввод пользователя
print(40 * '-' + '\n' + 'Введите ip-адрес по маске x.x.x.x/xx: ')
ip_and_mask = input()

#проверяем введенное значение по маске
#первый вариант if re.match(r'([0-9]{3}|[0-9]{2}|[0-9]{1})\.([0-9]{3}|[0-9]{2}|[0-9]{1})\.([0-9]{3}|[0-9]{2}|[0-9]{1})\.([0-9]{3}|[0-9]{2}|[0-9]{1})\/([0-9]{2}|[0-9]{2})', ip_and_mask) == None:
#второй вариант if re.match(r'\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}\/\d{,2}', ip_and_mask) == None:
if re.match(r'\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}\/\d{,2}', ip_and_mask) == None:
    print('Неверное значение')
    quit()
ip = separation_ip(ip_and_mask)
mask = separation_mask(ip_and_mask)

print(40 * '-' + '\n' + 'Network:' + '\n' + out_ip(ip, mask) + '\n\n' + 'Mask:' + '\n' + out_mask(mask) + '\n' + 40 * '-')
