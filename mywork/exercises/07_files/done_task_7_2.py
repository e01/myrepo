#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv
file_name = argv[1]
#file_name = "config_sw1.txt"
ignore = ['duplex', 'alias', 'Current configuration']

with open('{}'.format(file_name.strip())) as f:
    for line in f.readlines():
        if line.startswith('!'):
            pass
        else:
            if not(any(elem in line for elem in ignore)):
                    print(line.strip('\n'))
'''            for elem in ignore:
                if elem in line:
                        pass
                else:
                        print(line.strip('\n'))
'''
