li1 = [3,9,1,2,5,7,4,8,6]


def li_sort(li=li1):
    for i in range(len(li) -1):
        for j in range(i+1,len(li)):
            if li[i] > li[j]:
                li[i],li[j] = li[j],li[i]
    return li


res = li_sort()
print(res)


