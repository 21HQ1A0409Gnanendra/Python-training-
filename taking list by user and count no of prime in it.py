numbers = list(map(int, input("Enter integers separated by space: ").split()))
prime_count = 0
for num in numbers:
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            prime_count += 1

print(prime_count)
