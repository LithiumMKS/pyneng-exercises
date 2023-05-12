# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv


ignore = ["duplex", "alias", "configuration"]
file_input = argv[1]
file_output = argv[2]

with open(file_input) as src, open(file_output, 'w') as dst:
    for line in src:
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
                dst.write(line)
