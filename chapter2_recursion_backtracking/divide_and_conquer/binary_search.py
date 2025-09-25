def bs(l,s,e,x):
    e=min(e,len(l)-1) # allow to avoid index error

    if s<=e:
        mid=(s+e)//2
        if l[mid]==x:
            return mid 
        elif l[mid]>x:
            e=mid-1
        else:
            s=mid+1
        return bs(l,s,e,x)
    return -1 

l=[2,3,4,10,40,70]
x=90
print(bs(l,0,len(l),x))
print(bs(l,0,len(l)-1,x))

#39:00