import random

min = 0
max = 30
poskusov = 0
meja = 5

x = random.randrange(min, max)

while poskusov < meja:
	poskusov += 1

	ugibanje = int(input("Vnesi stevilo: "))

	if x == ugibanje:
		print("Cestitam, stevilo si ugotovil v ",
			poskusov, " poskusovih.")
		break
	elif x > ugibanje:
		print("Prenizko.")
	elif x < ugibanje:
		print("Previsoko.")

if poskusov >= meja:
	print("\nStevilo je bilo %d" % x)
