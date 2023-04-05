with open('a.txt','r+') as f:
    files_str = f.read().lower()
with open('a.txt','w+') as fe:
    fe.write(files_str)