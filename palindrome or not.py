n=int(input("enter num"))
n=str(n)
k=n[::-1] #[::-1] is used to reverse a sequence
if k==n:
    print("it is an palindrome")
else:
    print("it is not an palindrome")
