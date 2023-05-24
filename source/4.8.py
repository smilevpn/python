#тест ручного ввода
"""print ('Введите ip-адрес по маске x.x.x.x: ')
ip = input()"""
#докидывает в строку пробелы до 10 символов
def quantiti_symbols(value):
    return value + ((10 - len(value)) * ' ')
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
    res_bin += quantiti_symbols(format(x, '08b'))
    res_oct += quantiti_symbols(octets[i])
    i += 1

#выводим результат
print(res_oct + '\n' + res_bin)