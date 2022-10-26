#prastevila med 1 in 50
prime=[]

for x in range(0, 50+1):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
            else:
                prime.append(x)
                break
    else:
        if x == 1:
            prime.append(x)
print(prime)