max=10
n=0
if(max==0):
    print("Invalid input")
elif(max==1):
    print(1)
else: 
    for i in range(max+1):
        n+=i
    print(n)