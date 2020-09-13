n = int(input("numero "))
if n == 1:
    print("not prime")
    raise SystemExit
for i in range (2, int(n/2)):
    if n % i == 0:
        print("not prime")
        raise SystemExit
    else:
        continue
print("prime")


