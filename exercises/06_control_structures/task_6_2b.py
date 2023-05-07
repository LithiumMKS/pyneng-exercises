# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес в формате 10.0.1.1: ')
ip_correct = False
while not ip_correct:
    try:
        if ip == '0.0.0.0':
            print('unassigned')
            break
        elif ip == '255.255.255.255':
            print('local broadcast')
            break
        elif int(ip.split('.')[0]) in range(1, 224) \
            and int(ip.split('.')[1]) in range(0, 256) \
            and int(ip.split('.')[2]) in range(0, 256) \
            and int(ip.split('.')[3]) in range(0, 256) \
            and len(ip.split('.')) == 4:
            print('unicast')
            break
        elif int(ip.split('.')[0]) in range(224, 240) \
            and int(ip.split('.')[1]) in range(0, 256) \
            and int(ip.split('.')[2]) in range(0, 256) \
            and int(ip.split('.')[3]) in range(0, 256) \
            and len(ip.split('.')) == 4:
            print('multicast')
            break
        elif int(ip.split('.')[0]) in range(241, 256) \
            and int(ip.split('.')[1]) in range(0, 256) \
            and int(ip.split('.')[2]) in range(0, 256) \
            and int(ip.split('.')[3]) in range(0, 256) \
            and len(ip.split('.')) == 4:
            print('unused')
            break
        else:
            print('Неправильный IP-адрес')
            ip = input('Введите IP-адрес в формате 10.0.1.1: ')
    except:
        print('Неправильный IP-адрес')
        ip = input('Введите IP-адрес в формате 10.0.1.1: ')
