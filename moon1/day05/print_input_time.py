

def input_time(input_str='z'):
    key_list = ['azc','dwf','gti','jql','mon','pkr','shu','vex','yb']
    count_time = 0
    if len(input_str) >16:
        print('输入无效')
        return 0
    else :
        for i in input_str:
            for j in key_list:
                if i in j:
                    if input_str[input_str.index(i) - 1] in j and input_str.index(i) > 0:
                        if j.index(i) == 0:
                            count_time += 3
                        elif j.index(i) == 1:
                            count_time += 4
                        else:
                            count_time += 5
                        print(i,j)
                    else:
                        if j.index(i) == 0:
                            count_time += 1
                        elif j.index(i) == 1:
                            count_time += 2
                        else:
                            count_time += 3
                        print(i,j)

        return count_time


res = input_time()
print(res)
























