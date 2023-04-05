import random

li = []
for i in range(10):
    li.append(random.randint(0,10))
with open('a.txt','w+') as f:
    f.write(str(li))

















