ip = '127.0.0.1'


def is_ip(ip=ip):
    str_ip = ''
    if ip.count('.') == 3:
        ip_list = ip.split('.')
        for i in ip_list:
            str_ip+= i
        try:
            int(str_ip)
        except Exception:
            return False
        else:
            return True
    else:
        return False


res = is_ip()
print(res)













