l=[None]*10
l2=[11,21,2,3,4,55,66,677,45]
for i in l2:
    if l[i%10]==None:
        l[i%10]=i
    else:
        a=i%10
        while l[a]!=None:
            a+=1
        l[a]=i
print(l)