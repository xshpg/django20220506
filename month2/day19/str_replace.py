int_str = input("请输入数字：")
chu_li =[]
for i in int_str:
    j = (int(i)+3)%9
    chu_li.append(str(j))
chu_li[0],chu_li[2]=chu_li[2],chu_li[0]
chu_li[1],chu_li[3]=chu_li[3],chu_li[1]
new_str = ''
for i in chu_li:
    new_str+= i
print(new_str)

