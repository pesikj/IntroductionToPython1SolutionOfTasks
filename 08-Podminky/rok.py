rok = input("Zadej rok: ")
rok = int(rok)
if rok % 4 == 0:
  if rok % 100 == 0:
    if rok % 400 == 0:
      print("Rok je přestupný.")
    else:
      print("Rok není přestupný")
  else:
    print("Rok je přestupný.")
else:
  print("Rok není přestupný.")

"""
Alternativní řešení pomocí klíčových slov and a or.

Klíčová slova and a or jsou popsaná zde: 
http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2
"""

if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
  print("Rok je přestupný.")
else:
  print("Rok není přestupný")