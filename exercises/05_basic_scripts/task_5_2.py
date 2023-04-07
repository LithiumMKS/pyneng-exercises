# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

net_str = input('Введите IP-сети в формате "10.1.1.0/24": ')
net = net_str.split('/')[0]
net_okt1, net_okt2, net_okt3, net_okt4 = net.split('.')[0], net.split('.')[1], net.split('.')[2], net.split('.')[3]

print('Network:')
print('{:<10}{:<10}{:<10}{:<10}'.format(net_okt1, net_okt2, net_okt3, net_okt4))
print('{:>08b}  {:>08b}  {:>08b}  {:>08b}'.format(int(net_okt1), int(net_okt2), int(net_okt3), int(net_okt4)))

mask = net_str.split('/')[1]
mask_bin_str = '1' * int(mask) + "0" * (32-int(mask))
mask_bin_str_1 = mask_bin_str[0:8]
mask_bin_str_2 = mask_bin_str[8:16]
mask_bin_str_3 = mask_bin_str[16:24]
mask_bin_str_4 = mask_bin_str[24:32]
print('Mask:')
#print(mask_bin_str)
#print(mask_bin_str_1)
#print(mask_bin_str_2)
#print(mask_bin_str_3)
#print(mask_bin_str_4)

print('/'+mask)
print('{:<10}{:<10}{:<10}{:<10}'.format(int(mask_bin_str_1,2), int(mask_bin_str_2, 2), int(mask_bin_str_3, 2), int(mask_bin_str_4, 2)))
print('{:>08}  {:>08}  {:>08}  {:>08}'.format(mask_bin_str_1, mask_bin_str_2, mask_bin_str_3, mask_bin_str_4))
