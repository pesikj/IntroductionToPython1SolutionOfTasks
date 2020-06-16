"""
Klíčová slova and a or jsou popsaná zde: 

http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2
"""

cislo = input("Zadej čislo: ")
cislo = int(cislo)

if cislo == 0:
  print("Číslo je 0.")
else:
  if cislo % 2 == 0:
    print("Číslo je sudé.")
  else:
    print("Číslo je liché.")
  if cislo <= 10 or (cislo >= 19 and cislo <= 28):
    if cislo % 2 == 0:
      print("Číslo je černé.")
    else:
      print("Číslo je červené.")
  else:
    if cislo % 2 == 1:
      print("Číslo je černé.")
    else:
      print("Číslo je červené.")
