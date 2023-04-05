

def func(list1=[1,2,3,4,5,6,7,8],list2=[11,1,5,6,7,12,15,20]):
    strs = ''
    if len(list1) <= len(list2):
        for i in list1:
            if i in list2:
                strs+=str(i)
        return strs
    else:
        for i in list2:
            if i in list1:
                strs+=str(i)
        return strs


res = func()
print(res)












