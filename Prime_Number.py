def Prime(n):
    i=n-1
    c=0
    while(i>1):
        if(n%i==0):
            c+=1 
        i-=1
    if(c>0):
        return 0
    return 1

max=10
print("Prime number upto 10")
if(max==1):
    print(max)
elif(max==0):
    print("Invalid input")
else:
    print(1,end=" ")
    for i in range(2,max+1):
        if(Prime(i)):
            print(i,end=" ")
    