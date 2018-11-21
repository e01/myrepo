# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_file='config_sw2.txt'):
    with open(config_file) as f:
        cfg_lines = f.readlines()
        vlan1_ports={}
        trunk_dict={}
        access_dict={}
        for line in f:
            if line.startswith('interface FastEthernet'):
                intf_name = line.rstrip()
                continue
            elif line.startswith(' switchport trunk allowed vlan'):
                 trunk_vlans = [int(elem) for elem in line.lstrip(" switchport trunk allowed vlan").rstrip().split(',')]
                 trunk_dict[intf_name]= trunk_vlans
                 continue
            elif line.startswith(" switchport access vlan"):
                 access_vlan = int(line.lstrip(" switchport access vlan").rstrip())
                 access_dict[intf_name] = access_vlan
            elif line.startswith("  switchport mode access"):
                 continue
                 if line.startswith(" duplex auto"):
                    vlan1_ports[intf_name] = 1
                    continue
            else:
                continue
        return trunk_dict, access_dict, vlan1_ports

a,b,c = get_int_vlan_map()
print(a)
print(b)
print(c)