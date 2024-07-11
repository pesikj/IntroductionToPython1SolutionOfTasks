"""
Klíčová slova and a or jsou popsaná zde: 

https://kodim.cz/czechitas/uvod-do-progr-1/prvni-krucky/podminky/cteni-na-doma
"""

cislo = input("Zadej čislo: ")
cislo = int(cislo)

if cislo == 0:
    print("Číslo je 0.")
    exit()

if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

if cislo <= 10:
    if cislo % 2 == 0:
        print("Číslo je černé.")
    else:
        print("Číslo je červené.")
elif cislo <= 19:
    if cislo % 2 == 1:
        print("Číslo je černé.")
    else:
        print("Číslo je červené.")
elif cislo <= 28:
    if cislo % 2 == 0:
        print("Číslo je černé.")
    else:
        print("Číslo je červené.")
else:
    if cislo % 2 == 1:
        print("Číslo je černé.")
    else:
        print("Číslo je červené.")

# Alternativní řešení

cislo = input("Zadej čislo: ")
cislo = int(cislo)

if cislo == 0:
  print("Číslo je 0.")
  exit()
if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")
if cislo <= 10:
    if cislo % 2 == 0:
        print("Číslo je černé.")
    else:
        print("Číslo je červené.")
elif 19 <= cislo <= 28:
    if cislo % 2 == 0:
        print("Číslo je černé.")
    else:
        print("Číslo je červené.")
else:
    if cislo % 2 == 1:
        print("Číslo je černé.")
    else:
        print("Číslo je červené.")
