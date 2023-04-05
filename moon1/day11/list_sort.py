li = [-5,8,0,4,9,-4,-2,0,-2,8,2,-4]


def li_sort(li1=li):
    positive_list = []
    minus_list = []
    for i in li1:
        if i >= 0:
            positive_list.append(i)
        else:
            minus_list.append(i)
    positive_list.sort()
    minus_list.sort(reverse=True)
    return positive_list+minus_list


res = li_sort()
print(res)










