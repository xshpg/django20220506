a = [1,2,3,4,5,6,7,8,9,1]

def func_count(li=a):
    li_dict = {}
    for i in li:
        li_dict[i] = li.count(i)
    return li_dict


res = func_count()
print(res)














