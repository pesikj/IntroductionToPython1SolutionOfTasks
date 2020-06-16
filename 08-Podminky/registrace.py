uzivatelskeJmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
heslo2 = input("Zadej heslo znovu: ")
if heslo != heslo2:
  print("Hesla se neshodují.")
elif len(heslo) <= 8:
  print("Heslo je příliš krátké")
