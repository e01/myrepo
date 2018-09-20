#!/usr/bin/env python

#ip_net = input('Please enter IP network ' )
#ip, mask = ip_net.split('/')
from sys import argv
ip_net = str(argv[1])
ip, mask = ip_net.split('/')
#print(mask)
#print(ip)

bin_mask = '1'*int(mask)+'0'*(32-int(mask))
bin_mask_octets = [bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:32]]
 
ip1,ip2,ip3,ip4 = int(ip.split('.')[0]),int(ip.split('.')[1]),int(ip.split('.')[2]),int(ip.split('.')[3])
mask1,mask2,mask3,mask4 = [int(bin_mask[0:8],2), int(bin_mask[8:16],2), int(bin_mask[16:24],2), int(bin_mask[24:32],2)]
 
net1,net2,net3,net4 = int(bin(ip1),2) & int(bin(mask1),2), int(bin(ip2),2) & int(bin(mask2),2), int(bin(ip3),2) & int(bin(mask3),2), int(bin(ip4),2) & int(bin(mask4),2)
 
output_template = '''
 Network:
 {0:<8} {1:<8} {2:<8} {3:<8}
 {0:08b} {1:08b} {2:08b} {3:08b}
 
 Mask:
 {4:<8} {5:<8} {6:<8} {7:<8}
 {4:08b} {5:08b} {6:08b} {7:08b}
 '''


print(output_template.format(net1,net2,net3,net4,mask1,mask2,mask3,mask4))


