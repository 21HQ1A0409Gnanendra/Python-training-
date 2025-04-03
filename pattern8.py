n=int(input("enter input"))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*i+1,2*n):
        print("*",end="")
    print()
