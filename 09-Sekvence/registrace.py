uzivatelskeJmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
heslo2 = input("Zadej heslo znovu: ")
# Pro urychlení běhu programu tento kód zakomentujeme
# if heslo != heslo2:
#   print("Hesla se neshodují.")
# elif len(heslo) <= 8:
#   print("Heslo je příliš krátké")

email = input("Zadej email: ")
spravny = True
if len(email) <= 5:
  print("Email je moc krátký")
  spravny = False
if "." not in email:
  print("Chybí tečka.")
  spravny = False
if "@" not in email:      
  print("Chybí zavináč.")
  spravny = False
if spravny == True:
  print("Email je ok.")
