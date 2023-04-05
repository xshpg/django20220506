

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return func(n - 1) + func(n - 2)


def sum_grade(n):
    sum = 0
    for i in range(1,n+1):
       sum += func(i) / func(i+1)
    return sum
res = sum_grade(10)
print(res)












