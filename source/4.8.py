#тест ручного ввода
"""print ('Введите ip-адрес по маске x.x.x.x: ')
ip = input()"""

#входящие данные, переменная ip
ip = "192.168.3.1" 
#делим ip на части с разделителем
octets = ip.split('.')
#инициализируем счетчик
i = 0
#инициализируем строки
res_bin, res_oct = '', ''
#перебираем каждый элемент с преобразованием в двоичный код с форматированием вывода
while i < len(octets):
    x = int(octets[i])
    res_bin += format(x, '08b') + '  '
    if len(octets[i]) == 3:
        res_oct += octets[i] + '       '
    elif len(octets[i]) == 2:
        res_oct += octets[i] + '        '
    else:
        res_oct += octets[i] + '         '
    i += 1

#выводим результат
print(res_oct + '\n' + res_bin)