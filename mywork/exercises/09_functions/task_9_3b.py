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
    ''' Checks config and filter access and trunk VLANs from interface'''
    with open(config_file) as f:
        cfg_lines = f.readlines()
        vlan1_ports = {}
        trunk_dict = {}
        access_dict = {}
        for line in range(0,len(cfg_lines)):
            if cfg_lines[line].startswith('interface FastEthernet'):
                intf_name = cfg_lines[line].rstrip()
                continue
            elif cfg_lines[line].startswith(' switchport trunk allowed vlan'):
                trunk_vlans = [int(elem) for elem in cfg_lines[line].lstrip(" switchport trunk allowed vlan").rstrip().split(',')]
                trunk_dict[intf_name] = trunk_vlans
                continue
            elif cfg_lines[line].startswith(" switchport access vlan"):
                access_vlan = int(cfg_lines[line].lstrip(" switchport access vlan").rstrip())
                access_dict[intf_name] = access_vlan
            elif cfg_lines[line].startswith(" switchport mode access") and cfg_lines[line + 1].startswith(" duplex auto"):
                access_dict[intf_name] = 1
                continue
            else:
                continue
        return trunk_dict, access_dict


a, b = get_int_vlan_map()
print(a)
print(b)
