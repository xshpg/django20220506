
def func(strs='1234'):
    try:
        int_num = int(strs)
    except ValueError as e:
        print('不是数字字符串，转化失败')
        raise e
    else:
        return int_num


res = func(strs=' ')
print(res)

















