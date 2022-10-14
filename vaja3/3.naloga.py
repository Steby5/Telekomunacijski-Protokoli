a=input("Vnesi prvo celo stevilo: ")
b=input("Vnesi drugo celo stevilo: ")
c=input("Vnesi tretje celo stevilo: ")

print(a, type(a))
print(b, type(b))
print(c, type(c))

if a==b:
    print("Prvo in drugo stevilo sta enaki.")
else:
    print("Prvo in drugo stevilo nista enaki.")
if c<=a:
    print("Tretje stevilo je manjse ali enako prvemu.")
else:
    print("Tretje stevilo ni manjse ali enako prvemu.")