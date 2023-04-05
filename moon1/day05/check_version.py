def check_upgrade(old_version='v03.10.01.a',new_version='v05.01.08.b'):
    if old_version >= new_version:
        print('不升级')
    else:
        print('升级')

check_upgrade()












