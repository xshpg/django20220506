def search_max_num(li = ['a','b','a','b','a','c']):
    li_dict = {}
    for i in li:
        li_dict[i] = li.count(i)
    sort_res = sorted(li_dict.items(), key=lambda x: x[1], reverse=True)
    value_li = [sort_res[0][0]]
    count_li =[sort_res[0][1]]
    for i in sort_res[1:]:
        if sort_res[0][1] == i[1]:
            value_li.append(i[0])
    return value_li,count_li





res = search_max_num()
print(res)