import random
dolni_mez = input("Zadej dolní mez: ")
horni_mez = input("Zadej horní mez: ")
cislo = random.randint(int(dolni_mez), int(horni_mez))
print(cislo)