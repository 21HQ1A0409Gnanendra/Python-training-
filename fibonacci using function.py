def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input("enter the no.of required"))
fib(n)
