# -*- coding: utf-8 -*-
'''
Задание 7.3

Finds interfaces where there are more than one MAC

'''
import collections
with open("test.txt") as f:
    contents_list = f.readlines()
    intf_list = []
    for line in contents_list:
        if line.split()[3] == "CPU":
            pass
        else:
            intf = line.strip().split()[3]
            intf_list.append(intf)
    counter = dict(collections.Counter(intf_list))
    #print(counter)
    for elem in counter:
        if counter[elem] > 1:
            print(elem, ':', counter[elem])
    # b = {}
    # for item in intf_list:
    #     b[item] = b.get(item, 0) + 1
    # print(b)
