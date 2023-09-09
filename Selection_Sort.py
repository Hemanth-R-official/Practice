l=[-2,45,0,11,-9]
s=len(l)
n=0
for i in range(s-1):
    n+=1
    for j in range(i+1,s):
        n+=1
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
print(l,"No.of iterations ",n)
#By min value
l=[-2,45,0,11,-9]
n=0
m=min(l)
for i in range(s):
    n+=1
    if(l[i]>m):
        l[i],m=m,l[i]
l[s-1]=m
print(l,"No.of iterations ",n)