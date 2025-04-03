n=int(input("enter input"))
for i in range(n):
    for j in range(i+1,n):
        print(" ",end="")
    if i%2==0:
        for j in range(i+1):
            print(j+1,end="")
    else:
        for j in range(i+1,0,-1):
            print(j,end="")
    print()
    
