from moon1.day11.random_nums import randoms_str


def verfiy_code(codestr='64ssZ'):
    nums = codestr[2]
    try:
        int(nums)
    except Exception:
        return True
    else:
        return False




verfiy_code()







