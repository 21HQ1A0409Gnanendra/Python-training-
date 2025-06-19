n=int(input("enter num"))
k=0
for i in range(1,n):
    if n%i==0:
        k=k+i
if k==n:
    print("it is perfect number")
else:
    print("it is not an perfect number")
