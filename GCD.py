n = int(input("Enter a number: "))
n1 = int(input("Enter another number: "))
gcd = 1
i = 1
while i <= n and i <= n1:
    if n % i == 0 and n1 % i == 0:
        gcd = i
    i += 1
    print(f"HCF of {n} and {n1} = {gcd}")