
n = int(input("Enter a number: "))
prime = 1
if n <= 1:
    print("The number is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            prime = 0
            break
    if prime == 1:
        print("The number is prime")
    else:
        print("The number is not prime")