"""
Klíčová slova and a or jsou popsaná zde: 

http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2
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
    exit()
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