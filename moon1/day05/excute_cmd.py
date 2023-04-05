import os
import re

net_str = os.popen('ipconfig')
net_str1 = net_str.read()
# print(net_str1)
first_list = net_str1.split('\n')
# print(first_list)
excurat_list = []
for i in first_list:
    if first_list.index(i) > first_list.index('无线局域网适配器 WLAN:'):
        excurat_list.append(i)
print(excurat_list[-2])
second_dict = {}
for i in excurat_list:
    if 'IPv6' in i:
        second_dict['ipv6'] = i.split('. : ')[1]
    elif 'IPv4' in i:
        second_dict['ipv3'] = i.split('. : ')[1]
    elif '默认网关' in i:
        second_dict['getewayip'] = i.split('. : ')[1]
print(second_dict)