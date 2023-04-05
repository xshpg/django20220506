

li1 = [8,6,4,3,9,1,2,5,7]
for i in range(len(li1) - 1):
    for j in range(i + 1,len(li1)):
        if li1[i] > li1[j]:
            li1[i],li1[j] = li1[j],li1[i]
print(li1)






