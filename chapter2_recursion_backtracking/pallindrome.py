def check_palin(s):
    if len(s)==0:
        return True 
    else:
        return s[0]==s[-1] and check_palin(s[1:-1])
    
print(check_palin("malayalam"))
print(check_palin("a"))
print(check_palin("ashu"))
print(check_palin("kayak"))