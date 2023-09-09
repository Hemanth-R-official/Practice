#l1=list(map(int,input().split(' ')))
#l2=list(map(str,input().split(' ')))
#l3=input()
l1=[1,2,3,4,5]
#l2=l1 #call by referrence
l2= [i for i in l1] #call by value
l2.remove(3)
#print(len(l1))
#print(len(l2))
#print(len(l3))
print("List 1")
for i in l1:
    print(i, end=' ')
print("\nList 2")
for i in l2:
    print(i,end=' ')