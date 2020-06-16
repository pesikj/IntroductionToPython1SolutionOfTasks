print("Divadlo Pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")
uzivatelskeJmeno = input("Zadej uživatelské jméno: ")
vek = input("Zadej věk: ")
vek = int(vek)
plnaCena = 12
if vek < 6:
  cena = 0
elif vek <= 26:
  cena = plnaCena * (1 - 0.65)
elif vek <= 64:
  cena = plnaCena
else:
  cena = plnaCena * 0.5
cena = round(cena, 2)
print(f"Cena vstupenky je {cena}.")
print("Cena vstupenky je " + str(cena) + ".")