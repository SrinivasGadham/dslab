l=[int(i) for i in input("Enter the values:").split()]
n=len(l)
def quick(l,first,last):
    if(first<last):
        pivot=first
        i=first
        j=last
        while(i<j):
            while(l[pivot]>=l[i] and i<last):
                i+=1
            while(l[pivot]<l[j]):
                j-=1
            if(i<j):
                l[i],l[j]=l[j],l[i]
            else:
                l[pivot],l[j]=l[j],l[pivot]
        quick(l,first,j-1)
        quick(l,j+1,last)
    return l
print(quick(l,0,n-1))
print(l)