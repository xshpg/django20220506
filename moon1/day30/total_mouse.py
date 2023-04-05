
def sum_mouse(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif 3 <= n and n <= 9:
        return sum_mouse(n-1)+sum_mouse(n-2)
    elif n == 10:
        return sum_mouse(n-1)+sum_mouse(n-2) -1
    elif n == 11:
        return sum_mouse(n-1)-1+sum_mouse(n-2)
    else:
        return sum_mouse(n-1)+sum_mouse(n-2)-(sum_mouse(n-11))


res = sum_mouse(12)
print(res)






















