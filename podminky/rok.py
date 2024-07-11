rok = input("Zadej rok: ")
rok = int(rok)
if rok % 4 != 0:
  print("Rok není přestupný")
  exit()
# Zde využíváme vnořenou podmínku - podmínku uvnitř podmínky
if rok % 100 == 0:
  if rok % 400 == 0:
    print("Rok je přestupný.")
  else:
    print("Rok není přestupný")
else:
  print("Rok je přestupný.")

"""
Alternativní řešení pomocí klíčových slov and a or.

Klíčová slova and a or jsou popsaná zde: 
https://kodim.cz/czechitas/uvod-do-progr-1/prvni-krucky/podminky/cteni-na-doma
"""

if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
  print("Rok je přestupný.")
else:
  print("Rok není přestupný")
