print("Fibonacci numbers upto 10 numbers")
a=0
b=1
max=10
print (a, end=" ")
for i in range(0,max):
    print(a,end=" ")
    a,b=b,a+b
print("\nFibonacci numbers below 10")
a,b=0,1
while(a<max):
    print(a,end=" ")
    a,b=b,a+b
