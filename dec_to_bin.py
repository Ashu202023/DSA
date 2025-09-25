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