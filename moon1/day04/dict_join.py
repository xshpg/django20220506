

# keys = ['A','B','C']
# values = ['1','2','3']
# print(dict(zip(keys,values)))

# list_1 = ['a','b','c','1','A','winning']
# list_2 = ['a','python','string','1']
# print(list(set(list_1+list_2)))

a = [{'x':1,'y':2},{'x':2,'y':3},{'x':3,'y':4}]

for i in range(len(a) - 1):
    for j in range(i,len(a)):
        if a[i]['x'] < a[j]['x']:
            a[i],a[j]=a[j],a[i]
print(a)











