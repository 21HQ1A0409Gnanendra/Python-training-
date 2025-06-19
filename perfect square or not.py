n=int(input("enter num"))
for i in range(n+1):
    if i*i==n:
        print("perfect square")
        break
else:
    print("not perfect square")
