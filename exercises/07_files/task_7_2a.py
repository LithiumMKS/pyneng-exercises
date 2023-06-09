# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv


ignore = ["duplex", "alias", "configuration"]

file = argv[1]

with open(file) as f:
    for line in f:
        if line.startswith('!'):
            flag = False
        else:
            flag = False
            for i in ignore:
                if line.find(i) != -1:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                print(line.strip('\n'))




