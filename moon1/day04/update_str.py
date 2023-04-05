
def rpad(src='abcde',lens=3,str1='123'):
    if len(src) < lens:
        while len(src) < lens:
            for i in str1:
                if len(src) < lens:
                    src += i
        return src
    elif len(src) == lens:
        return str1
    else:
        return src[:len(src) - lens + 1]


res = rpad()
print(res)






