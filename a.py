"""
求元组中重复最多的元素
"""

def findmosttopn(words,n=3):
    from collections import Counter
    word_counts = Counter(words)
    return word_counts.most_common(n)



res = findmosttopn([1,2,3,4,2,3,1,2])
print(res)


List=[1,2,3,4,5,3,2,1,4,5,6,4,2,3,4,6,2,2]
a = {}
for i in List:
    if List.count(i)>1:
        a[i] = List.count(i)
a = sorted(a.items(), key=lambda item:item[0])
print (a)

