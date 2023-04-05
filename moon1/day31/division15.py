sum =0
count = 0
strnum = ' '
for i in range(100,10000):
    for j in str(i):
        sum += int(j)
        if sum%15 ==0:
            strnum +=str(i)+' '
            count+=1
            if count == 10:
                print(strnum)
                count = 0
                strnum = ' '














