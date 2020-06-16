heslo = "superTajneHeslo123."

znak = input("Zadej 2. znak hesla: ")
if znak != heslo[1]:
  print("Chyba ověření.")
  exit()
znak = input("Zadej 5. znak hesla: ")
if znak != heslo[4]:
  print("Chyba ověření.")
  exit()
znak = input("Zadej 7. znak hesla: ")
if znak != heslo[6]:
  print("Chyba ověření.")
  exit()
print("Ověření bylo úspěšné!")