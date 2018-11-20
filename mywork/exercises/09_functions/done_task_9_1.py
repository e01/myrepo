#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 9.1

Создать функцию, которая генерирует конфигурацию для access-портов.

Функция ожидает, как аргумент, словарь access-портов, вида:
    { 'FastEthernet0/12':10,
      'FastEthernet0/14':11,
      'FastEthernet0/16':17,
      'FastEthernet0/17':150 }

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_template.
Заготовка для функции уже сделана.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]

Проверить работу функции на примере словаря access_dict.


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''



access_dict = {
        'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17,
        'FastEthernet0/17': 150
    }


def config_interface(intf_name, vlan):
    result=[]
    interface = 'interface {}'
    access_template = [
        'switchport mode access', 'switchport access vlan {}',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    result.append(interface.format(intf_name))
    for commands in access_template:
        result.append(commands.format(vlan))
    return result


def generate_access_config(access=access_dict):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    result = []
    for key in access:
        result.extend(config_interface(key, access[key]))
    return result

print(generate_access_config())


