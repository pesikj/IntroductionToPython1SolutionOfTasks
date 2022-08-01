uzivatelskeJmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
if heslo != "simsalabim":
  print("Vstup nepovolen!")
  exit()
vek = input("Zadej věk: ")
vek = int(vek)
if vek > 18:
  print("Smíš vstoupit.")
else:
    print("Vstup nepovolen")
