a = 'AAABBCDCEE'
first_str = a[0]
str1= ''
second_str = ''
for i in a:
    if i == first_str:
        str1+=i
    else:
        first_str = i
        str1+='.'+i
str_li = str1.split('.')
strs = ''
for i in str_li:
    strs+=str(len(i))+i[0]
print(strs)





































