
while True:
    phone = input('请输入手机号：')
    if phone[0] == '1' and len(phone)==11 and phone.isdecimal():
        print(phone)
    else:
        print("请输入1开头的11位数字")

























