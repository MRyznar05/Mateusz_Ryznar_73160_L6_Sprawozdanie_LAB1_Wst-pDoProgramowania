print("A1")
x = 1+2 #   dodawanie liczb całkowitych
print(type(x), "\n", x,"\n") #    typ int i wynik

print("A2")
x = 1+4.5 #   dodawanie liczby całkowitej do zmiennoprzecinkowej
print(type(x), "\n", x,"\n") #    typ float i wynik

print("A3")
x = 3/2 #   dzielenie dwóch liczb całkowitych
print(type(x), "\n", x,"\n") #    typ float i wynik

print("A4")
x = 4/2 #   dzielenie dwóch liczb całkowitych
print(type(x), "\n", x,"\n") #    typ float (ponieważ jest to wynik dzielenia i nawet jeśli jest całkowity to pozostanie float) i wynik

print("A5")
x = 3//2 #   dzielenie dwóch liczb całkowitych z odrzuceniem reszty
print(type(x), "\n", x,"\n") #    typ int i wynik

print("A6")
x = -3//2 #   dzielenie dwóch liczb całkowitych z odrzuceniem reszty a wynik jest zaokrąglany w dół czyli do mniejszej liczby całkowitej
print(type(x), "\n", x,"\n") #    typ int i wynik

print("A7")
x = 11%2 #  obliczenie reszty z dzielenia
print(type(x), "\n", x,"\n") #  typ int i wynik

print("A8")
x = 2**10 # potęgowanie liczby 2 do 10
print(type(x), "\n", x,"\n") #  typ int i wynik

print("A9")
x = 8**(1/3) # potęgowanie liczby 8 do potęgi ułamka 1/3
print(type(x), "\n", x,"\n") #  typ float i wynik

print("B1")
print(int(3.0)) #   zamiana liczby zmiennoprzecinkowej na całkowitą

print("B2")
print(float(3)) #   zamiana liczby całkowitej na zmiennoprzecinkową

print("B3")
print(float("3")) #   zamiana z typu ciągu znaków na typ zmiennoprzecinkowy
# dowod
print(type("3"), "\n", type(float("3")))

print("B4")
print(str(12.4)) #  zamiana z typu zmiennoprzecinkowego na ciąg znaków

print("B5")
print(bool(0)) # każda wartość instrukcji bool poza 0 jest uznawana za true
#   dowód
import random
x = random.randint(1, 10)
print(x)
print(bool(x))
