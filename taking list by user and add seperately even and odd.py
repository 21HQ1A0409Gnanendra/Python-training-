numbers = list(map(int, input("Enter integers separated by space: ").split()))
odd=0
even=0
for num in numbers:
    if num%2==0:
        even+=num
    else:
        odd+=num
print(odd)
print(even)
