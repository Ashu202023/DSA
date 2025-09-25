def ran_base_k(n):
    l=[]
    for i in range(n):
        l.append(str(i))
    return l

def str_base_k(n,k):
    if n==0:
        return [""]
    elif n==1:
        return ran_base_k(k)
    else:
        # return [i+j for i in ran_base_k(k) for j in str_base_k(n-1,k)]
        result=[]
        for i in ran_base_k(k):
            for j in str_base_k(n-1,k):
                result.append(i+j)
        return result
print(str_base_k(3,2))