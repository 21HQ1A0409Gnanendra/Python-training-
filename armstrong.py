n=int(input("enter the number"))
length=len(str(n))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**length
    temp=temp//10
if sum==n:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")

