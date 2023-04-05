

a = [1,2,3,4,5,6,7,8,9]
def func(x):
    return x%2 ==1
print(list(filter(func,a)))