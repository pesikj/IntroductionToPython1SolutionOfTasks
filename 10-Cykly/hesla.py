hesla = [
  'xyz101',
  'punťa',
  'razor-blade',
  '1234',
  '12011986',
  'martin111',
  'trhnisi',
  'hokuspokus',
  'jeník15',
  'kristus-te-spasi',
  'beruška',
  'strčprstskrzkrk'
]
# b
for heslo in hesla:
  print(heslo)
# c
for heslo in hesla:
  if len(heslo) > 8:
    print(heslo)
# d
for heslo in hesla:
  if "-" in heslo:
    print(heslo)