def frults_nums(n):
    if n == 10:
        return 1
    elif 0<n <10:
        return (frults_nums(n+1)+1) * 2
    else:
        return None


res = frults_nums(n=1)
print(res)















