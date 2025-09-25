def rev_string(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+rev_string(s[:-1])

print(rev_string("the simple engineer."))
