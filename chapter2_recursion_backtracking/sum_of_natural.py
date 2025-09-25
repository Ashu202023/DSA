def sum_of_natural_num(n):
    if n==0 or n==1:
        return n
    else:
        return n+sum_of_natural_num(n-1)
    
print(sum_of_natural_num(5))
print(sum_of_natural_num(10))
print(sum_of_natural_num(0))
print(sum_of_natural_num(1))
print(sum_of_natural_num(100))