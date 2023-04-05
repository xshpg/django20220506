def freely_hight(n):
    if n == 1:
        return 100
    else:
        return 100 * (1/2)**(n - 1) * 2
total_distace = 0
for i in range(1,11):
    total_distace += freely_hight(i)
print(total_distace)

























