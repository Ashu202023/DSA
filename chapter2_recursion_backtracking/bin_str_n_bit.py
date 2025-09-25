def appendatbeg(x,s):
    return [x+ i for i in s]
def bin_str_n_bit(n):
    if n==0:
        return [""]
    elif n==1:
        return ["0","1"]
    else:
        return appendatbeg("0",bin_str_n_bit(n-1))+appendatbeg("1",bin_str_n_bit(n-1))

print(bin_str_n_bit(3))
print(bin_str_n_bit(4))
print(bin_str_n_bit(5))
print(bin_str_n_bit(2))