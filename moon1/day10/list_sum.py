nums = [1,2,2,3,4,5]
m = 6


def get_element(num =nums,n=m):
    element_list = []
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == n and i != j:
                element_list.append((num[i],num[j],i,j))
    return element_list


res = get_element()
print(res)

























