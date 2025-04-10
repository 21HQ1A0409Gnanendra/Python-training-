def fact(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    print(c)
n=int(input("enter the number"))
fact(n)
