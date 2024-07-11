num = int(input("Enter a number: "))

# Start with the smallest prime number
divisor = 2   

# Find prime factors and print them
print("Prime factors of", num, "are:", end=' ')
while num > 1:
    if num % divisor == 0:
        print(divisor, end=' ')
        num //= divisor     # Update num by dividing it by the divisor
    else:
        divisor += 1 