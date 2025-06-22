numbers = list(map(int, input("Enter integers separated by space: ").split()))
repeat=[]
for num in numbers:
    if num not in repeat:
        repeat.append(num)
    else:
        print(num)
        break
        
