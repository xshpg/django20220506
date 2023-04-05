import random,string



def randoms_str():
    num_str = str(random.randint(0,100))
    strs = ''
    if len(num_str) == 1:
        for i in range(4):
            str1 = random.choice(string.ascii_letters)
            strs+=str1
        return num_str+strs
    else:
        for i in range(3):
            str2 = random.choice(string.ascii_letters)
            strs+=str2
        return num_str+strs



res = randoms_str()
print(res)

















