def Factorial(n):
    i=n-1
    while(i>0):
        n*=i
        i-=1
    return n
max=10
if(max==0):
    print("Invalid input")
elif(max==1):
    print(1)
else:
    print(1,end=" ")
    for i in range(2,max):
        print(Factorial(i),end=" ")