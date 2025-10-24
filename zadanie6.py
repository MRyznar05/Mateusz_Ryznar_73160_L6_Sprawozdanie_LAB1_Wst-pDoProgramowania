droga = float(input("Podaj ilość kilometrów: "))
spalanie = float(input("Podaj średnie spalanie: "))
zuzycie_paliwa = droga*spalanie/100
koszta = zuzycie_paliwa*6.5
print("Zużycie paliwa", round(zuzycie_paliwa, 2),"L")
print("Koszt drogi", round(koszta, 2),"zł\n")

#Modyfikacja A)
import random
droga = random.randint(100,900)

spalanie = float(input("Podaj średnie spalanie: "))
cena_paliwa = float(input("Podaj aktualną cenę za litr paliwa: "))

zuzycie_paliwa = droga*spalanie/100
koszta = zuzycie_paliwa*cena_paliwa

print("Zużycie paliwa", round(zuzycie_paliwa, 2),"L")
print("Koszt drogi", round(koszta, 2),"zł\n")

#Modyfikacja B)

droga = random.randint(100,900)

spalanie = float(input("Podaj średnie spalanie: "))
cena_paliwa = float(input("Podaj aktualną cenę za litr paliwa: "))

zuzycie_paliwa = droga*spalanie/100
koszta = zuzycie_paliwa*cena_paliwa

print(f"Zużycie paliwa {round(zuzycie_paliwa, 2)}L")
print(f"Koszt drogi {round(koszta, 2)}L")

