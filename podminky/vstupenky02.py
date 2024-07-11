print("Divadlo Pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")
uzivatelske_jmeno = input("Zadej uživatelské jméno: ")
vek = input("Zadej věk: ")
vek = int(vek)
plna_cena = 12
if vek < 6:
  cena = 0
elif vek <= 26:
  cena = plna_cena * 0.65
elif vek <= 64:
  cena = plna_cena
else:
  cena = plna_cena * 0.5
cena = round(cena, 2)
print(f"Cena vstupenky je {cena}.")
print("Cena vstupenky je " + str(cena) + ".")
