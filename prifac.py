a = int(input("Enter a number: "))
count=0
for i in range(1,a):
    if a % i == 0:
        count += 1 
        lp = i 
if (count == 2):
    print("The number is prime")
else:
     print(a,"is composite")
print("Largest prime factor of",a,"is",lp)