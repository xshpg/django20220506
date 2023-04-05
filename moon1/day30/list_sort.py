li = ['a','b','c',1,2,3,3,1,4,5,2,5,3,4,'a']
li_dict = {}
for i in li:
    li_dict[i] = li.count(i)
# print(li_dict)
res = sorted(li_dict.items(),key=lambda x:x[1],reverse=True)
print(res)











