buy_way =0
for i in range(100):
    for j in range(100):
        for n in range(100):
            if (i * 5 + j *3 + n * 0.5 == 100) and i + j + n == 100:
                buy_way += 1
print(buy_way)












