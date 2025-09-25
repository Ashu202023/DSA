# 1st program: factorial of a number
def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans

print(factorial(5))

def fact_rec(n):
    if n==0:
        return 1
    else:
        return n*fact_rec(n-1)

print(fact_rec(5))

# 2nd program: reverse a string

def reverse(s):
    return s[::-1]

print(reverse("recursion"))

def rev_recursion(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+ rev_recursion(s[:-1])

print(rev_recursion("recursion"))

# check palindrome

def is_palindrome(s):
    s1=s[::-1]
    return s1==s

print(is_palindrome("abc"))
print(is_palindrome("madam"))

def rec_is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and rec_is_palindrome(s[1:-1])

print(rec_is_palindrome("abc"))
print(rec_is_palindrome("madam"))

# 4th program: array sum 

def sum(l):
    ans=0
    for i in l:
        ans+=i
    return ans

print(sum([1,2,3,4,5]))

def rec_sum(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+rec_sum(l[1:])

print(rec_sum([1,2,3,4,5]))

#Optimized recursion likhne ke liye slicing avoid kar sakte ho aur index pass kar sakte ho:

def rec_sum_optimized(l, i=0):
    if i == len(l):
        return 0
    return l[i] + rec_sum_optimized(l, i+1)

print(rec_sum_optimized([1,2,3,4,5]))

# 5th program: fibonacci series

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

# ye bahut slow hai, isme bahut saare same calls hote hain

# isko optimize karne ke liye hum memoization use kar sakte hain

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    elif n==0 or n==1:
        memo[n]=n
        return memo[n]
    else:
        memo[n]=fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
        return memo[n]

print(fibonacci_memo(10))

# 6th program: Print all elements of a list in reverse order using recursion (without actually reversing the list).
def print_reverse(l):
    if len(l)==0:
        return
    else:
        print(l[-1])
        print_reverse(l[:-1])

print_reverse([1,2,3,4,5])

#Optimized recursion (index based):
def print_reverse_safe(l, i=None):
    if i is None:
        i = 0
    if i == len(l):
        return
    print_reverse_safe(l, i+1)
    print(l[i])
print_reverse_safe([1,2,3,4,5])