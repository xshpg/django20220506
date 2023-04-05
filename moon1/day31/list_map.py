

li = [1,2,3,4,5]


def func(x):
    return x**2


res = list(map(func,li))
rest = [i for i in res if i>10]
print(rest)



























