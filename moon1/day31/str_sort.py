
s = 'ajldjlajfdljfddd'
sli = list(set(list(s)))
for i in range(len(sli)):
    for j in range(i+1,len(sli)):
        if sli[i] < sli[j]:
            sli[i],sli[j] == sli[j],sli[i]
print(sli)
strs = ''
for i in sli:
    strs+=i
print(strs)
















