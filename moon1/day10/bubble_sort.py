li1 = [1,2,1,4,6,2,3,4,9,3,0,5]

for i in range(len(li1) - 1):
    for j in range(i+1,len(li1)):
        if li1[i] > li1[j]:
            li1[i],li1[j] = li1[j],li1[i]


print(li1)














