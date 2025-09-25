def dectobin(n):
    if n==0 or n==1:
        return n
    else:
        return n%2 +10*(dectobin(n//2))
    
print(dectobin(13))
print(dectobin(8))
print(dectobin(0))
print(dectobin(1))
print(dectobin(7))

def dec_to_bin(s,r):
    if s==0:
        return r
    else:
        r=str(s%2)+r
        return dec_to_bin(s//2,r)
print(dec_to_bin(13,""))