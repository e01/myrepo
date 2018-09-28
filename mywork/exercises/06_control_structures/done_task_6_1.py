#! /usr/bin/env python

ip = input(' Please enter IP address: ')
octet_one = int(ip.split('.')[0])

if (octet_one > 1 and octet_one < 127) or (octet_one > 128 and octet_one < 191) or (octet_one > 192 and octet_one < 223):
    print('unicast')
elif (octet_one > 224 and octet_one < 239):
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

    
    
       

