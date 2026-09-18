n = int(input("Enter a number: "))
n1 = int(input("Enter another number: "))
lcm = 1
i = 1
while i <= n and i <= n1:
    if i % n == 0 and i % n1 == 0:
        lcm = i
        break
    i += 1
    print(f"LCM of {n} and {n1} = {lcm}")