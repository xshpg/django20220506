li = ['a','b','c','d','a']


def get_repetition(list1 =li):
    get_list = []
    li1 = list(set(li))
    for i in li:
        if li.count(i) > 1 and i not in get_list:
            get_list.append(i)
    return li1,get_list


res = get_repetition()
print(res)










