def func(str1='abcdefg',str2='aaabmncdefhi'):
    total_li = []
    if len(str1) <= len(str2):
        for i in range(len(str1)-1):
            strs = str1[i]
            for j in range(i+1,len(str1)):
                if strs in str2:
                    total_li.append(strs)
                    strs+=str1[j]
                else:
                    break
    else:
        for i in range(len(str2)-1):
            strs = str2[i]
            for j in range(i+1,len(str2)):
                if strs in str1:
                    total_li.append(strs)
                    strs+=str2[j]
                else:
                    break
    for i in range(len(total_li)-1):
        for j in range(i+1,len(total_li)):
            if len(total_li[i]) < len(total_li[j]):
                total_li[i],total_li[j]=total_li[j],total_li[i]
    return total_li[0]




res = func()
print(res)


















