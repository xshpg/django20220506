

def sort_list(list1):
    for i in range(len(list1) - 1):
        for j in range(i+1,len(list1)):
            if list1[i] > list1[j]:
                list1[i],list1[j]= list1[j],list1[i]
    return list1


res = sort_list(list1=[1,3,10,9,21,35,4,6])
print(res)
























