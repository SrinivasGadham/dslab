l=[int(i) for i in input("enter the elements:").split()]
n=len(l)
max=max(l)
pos=1
def radix(l,n,pos):
    count=[0]*10
    b=[0]*n
    for i in range(n):
        count[(l[i]//pos)%10]+=1
    for i in range(1,10):
        count[i]=count[i]+count[i-1]
    for i in range(n-1,-1,-1):
        b[count[(l[i]//pos)%10]-1]=l[i]
        count[(l[i] // pos) % 10] -= 1
    for i in range(n):
        l[i]=b[i]
    return l


while((max/pos)>0):
    radix(l,n,pos)
    pos=pos*10
print(l)