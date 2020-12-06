uzivatelskeJmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
heslo2 = input("Zadej heslo znovu: ")
# Pro urychlení běhu programu tento kód zakomentujeme
# if heslo != heslo2:
#   print("Hesla se neshodují.")
# elif len(heslo) <= 8:
#   print("Heslo je příliš krátké")

email = input("Zadej email: ")
if len(email) > 5:
  if "." in email:
    if "@" in email:
      print("Email je ok.")
    else:
      print("Chybí zavináč.")
  else:
    print("Chybí tečka.")
else:
  print("Email je moc krátký")
