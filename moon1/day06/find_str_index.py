str1 = 'abcaaxy12ab12'
def get_str_index(strs=str1):
    list1 = []
    for i,v in enumerate(str1):
        if str1.count(v) > 1:
            list1.append((v,i))
    return list1


res = get_str_index()
print(res)















