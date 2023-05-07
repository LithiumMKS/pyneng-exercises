# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес в формате 10.0.1.1: ')
if ip == '0.0.0.0':
    print('unassigned')
elif ip == '255.255.255.255':
    print('local broadcast')
elif int(ip.split('.')[0]) in range(1, 224) \
        and int(ip.split('.')[1]) in range(0, 256) \
        and int(ip.split('.')[2]) in range(0, 256) \
        and int(ip.split('.')[3]) in range(0, 256):
    print('unicast')
elif int(ip.split('.')[0]) in range(224, 240) \
        and int(ip.split('.')[1]) in range(0, 256) \
        and int(ip.split('.')[2]) in range(0, 256) \
        and int(ip.split('.')[3]) in range(0, 256):
    print('multicast')
else:
    print('unused')
