n=int(input("enter input"))
for i in range(n):
    for j in range(i+1):
        if i%2==1:
            print("@",end="")
        else:
            print(i+1,end="")
    print()
