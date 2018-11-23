#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
table_left = ['Protocol:','Prefix:','AD/Metric','Next-hop','Last update','Outbound interface']
with open('ospf.txt') as f:
    string_list = [line.rstrip() for line in f.readlines()]
    for elem in string_list:
        table_right = elem.split()
        table_right = [line.strip(",[]") for line in table_right]
        table_right.remove('via')
        if table_right[0] == 'O':
            table_right[0] = 'OSPF'
        else:
            table_right[0] = 'Unknown'
        result_dic = dict(zip(table_left,table_right))
        for field,value in result_dic.items():
            print('{0:<20} {1:<20}'.format(field,value))
        print('-'*40)
