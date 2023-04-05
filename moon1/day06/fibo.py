def feibo_num(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return feibo_num(num-1) + feibo_num(num-2)


for i in range(1,100):
    if feibo_num(i) <= 100:
        print(feibo_num(i))











