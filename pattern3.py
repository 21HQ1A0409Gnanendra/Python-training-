n=int(input("enter input"))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n):
        print("*",end="")
    print()
