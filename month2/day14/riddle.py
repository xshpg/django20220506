
def riddle_str(list1 = ['nwes','nesw','worlod'],list2=['news','world','worl']):
    answer_riddle = []
    for i in list1:
        for j in list2:
            if len(set(list(j))) == len(set(list(j+i))):
                answer_riddle.append((i,j))
    if answer_riddle:
        return answer_riddle
    else:
        return 'not found'



res = riddle_str()
print(res)
















