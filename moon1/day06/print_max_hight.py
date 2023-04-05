m = ['abc13','abv89','abcdef']
def func(a=m):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if len(a[i]) > len(a[j]):
                a[i],a[j] = a[j],a[i]
    str1 = ''
    for i in a[0]:
        center_list = []
        for j in a[1:]:
            for n in j:
                if a[0].index(i) == j.index(n):
                    center_list.append(n)
        if center_list.count(i) == len(a) - 1:
            str1 += str1.join(i)
    print(str1)


func()
























