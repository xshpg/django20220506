arr = ([
    4,5,9,4,1],
[
    11,14,9,6,20
],[
    21,44,90,16,21
       ],[
    16,34,99,600,230
       ],[
    121,18,89,60,33
       ])
arr_li = list(arr)
all_list = []
for i in arr_li:
    for n in i:
        all_list.append(n)
all_list.sort(reverse=True)
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
for i in range(len(all_list)):
    if i % 2 == 0:
        if len(a1) < 5:
            a1.append(all_list[i])
        elif len(a2) <5:
            a2.append(all_list[i])
        else:
            a3.append(all_list[i])
    else:
        if len(a6) < 5:
            a6.insert(0,all_list[i])
        elif len(a5) < 5:
            a5.insert(0,all_list[i])
        else:
            a4.insert(0,all_list[i])
sun_a = a3 + a4
a_ll = [a1,a2,sun_a,a5,a6]
print(tuple(a_ll))







