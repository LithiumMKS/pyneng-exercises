# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = int(input('Enter VLAN number: '))
fdb_temp = '{:<8} {:<19} {:<10}'
fdb_list = []
with open('CAM_table.txt') as f:
    for line in f:
        if line.find('Gi') != -1:
            line_list = line.split()
            if line_list[2] == 'DYNAMIC':
                poped_str = int(line_list.pop(0))
                line_list.insert(0, poped_str)
                line_list.remove('DYNAMIC')
                fdb_list.append(line_list)

for sublist in sorted(fdb_list):
    if sublist[0] == vlan:
        print(fdb_temp.format(str(sublist[0]), sublist[1], sublist[2]))
