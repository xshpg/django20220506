def total_rabbit(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return total_rabbit(n -1) + total_rabbit(n-2)


res = total_rabbit(n=10)
print(res)















