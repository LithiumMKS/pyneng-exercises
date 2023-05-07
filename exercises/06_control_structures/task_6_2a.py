# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес в формате 10.0.1.1: ')
try:
    if ip == '0.0.0.0':
        print('unassigned')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif int(ip.split('.')[0]) in range(1, 224) \
        and int(ip.split('.')[1]) in range(0, 256) \
        and int(ip.split('.')[2]) in range(0, 256) \
        and int(ip.split('.')[3]) in range(0, 256) \
        and len(ip.split('.')) == 4:
        print('unicast')
    elif int(ip.split('.')[0]) in range(224, 240) \
        and int(ip.split('.')[1]) in range(0, 256) \
        and int(ip.split('.')[2]) in range(0, 256) \
        and int(ip.split('.')[3]) in range(0, 256) \
        and len(ip.split('.')) == 4:
        print('multicast')
    elif int(ip.split('.')[0]) in range(241, 256) \
        and int(ip.split('.')[1]) in range(0, 256) \
        and int(ip.split('.')[2]) in range(0, 256) \
        and int(ip.split('.')[3]) in range(0, 256) \
        and len(ip.split('.')) == 4:
        print('unused')
    else:
        print('Неправильный IP-адрес')
except:
    print('Неправильный IP-адрес')
