a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if a == 0:
    if b != 0:
        print("Równanie sprzeczne")
    else:
        print("Równanie tożsamościowe")
else:
    x = -b/a
    print(x)

