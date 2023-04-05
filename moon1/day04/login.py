
passwd = {"admin":"123456","user1":"471258"}
i = 0
while i < True:
    name = input("请提示输入用户名：")
    if name in passwd:
        while i < 3:
            pwd = input("请输入密码：")
            i +=1
            if pwd == passwd[name]:
                print("登录成功")
            else:
                print("请输入正确密码,还有%s次机会"%(3-i))
        break
    else:
        print("请输入正确的用户名")






















