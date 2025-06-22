numbers = list(map(int, input("Enter integers separated by space: ").split()))
product_count = 1
for num in numbers:
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            product_count *= num

print(product_count)
