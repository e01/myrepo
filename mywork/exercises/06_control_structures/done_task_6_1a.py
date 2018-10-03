#! /usr/bin/env python
while 1:
    ip = input(' Please enter IP address: ')
    not_an_ip = False

    if len(ip.split('.')) == 4:
           for elem in ip.split('.'):
               if elem.isdigit():
                   pass
               else:
                    not_an_ip = True
                    break
    else:
          not_an_ip = True
    if len(ip.split('.'))== 4 and not(not_an_ip):
        octet_one = int(ip.split('.')[0])
        if (octet_one > 1 and octet_one < 127) or (octet_one > 128 and octet_one < 191) or (octet_one > 192 and octet_one < 223):
            print('unicast')
            break
        elif (octet_one > 224 and octet_one < 239):
            print('multicast')
            break
        elif ip == '255.255.255.255':
            print('local broadcast')
            break
        elif ip == '0.0.0.0':
            print('unassigned')
            break
        else:
            print('unused')
            break
    else:
        print("Wrong input - not an IP address")
        continue
    
    

    
    
       

