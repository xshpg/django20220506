
def max_and_min(li):
    max_value = max(li)
    max_count = li.count(max_value)
    min_value = min(li)
    min_count = li.count(min_value)
    res_list = [max_value,max_count,min_value,min_count]
    return res_list

res = max_and_min([1])
print(res)



