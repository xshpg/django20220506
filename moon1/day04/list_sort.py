def sort_nums(sort_li,n):
    li_dict = {}
    for i in sort_li:
        li_dict.update({i:sort_li.count(i)})
    res_list = sorted(li_dict.items(),key=lambda x:x[1],reverse=True)
    rest_li = []
    for i in res_list[:n]:
        rest_li.append(i[0])
    return rest_li


sest = sort_nums([1,2,3,4,1,2,5,2,1,7,1,4,4,4,4],3)
print(sest)






















