w=int(input("Enter the weight of watermelon:"))
if(w%2!=0):
    print("no it is odd")
else:
    x=w/2
    if(x%2==0):
        print("yes,brother 1 gets",x," brother 2 gets",x)
    else:
        print("yes,brother 1 gets",x-1,"brother 2 gets",x+1)
