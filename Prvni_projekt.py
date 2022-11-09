from collections import OrderedDict
'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Chovan
email: lukas.chovan@seznam.cz
discord: LachY22#8861
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
oddelovac = 40 * "-"

users = {"bob":"123", "ann":"pass123", "mike":"password132", "liz":"pass123"}

username = input("username: ")
password = input("password: ")

print(oddelovac)

registered = users.get(username) == password

if registered:
    print(f"Welcome to the app {username.capitalize()}!",
          f"We have 3 texts to be analyzed.",
          sep="\n")
else:
    print(f"Unregistered user, terminating the program..")
    quit()

print(oddelovac)

vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)

vycistena_slova = list()
jednotliva_slova = TEXTS[int(vyber_textu) - 1].split()

for slovo in jednotliva_slova:
    vycistena_slova.append(slovo.strip(",.:;!?"))

vyskyt_slov = dict()
for slovo in vycistena_slova:
    if slovo not in vyskyt_slov:
        vyskyt_slov[slovo] = 1
    else:
        vyskyt_slov[slovo] = vyskyt_slov[slovo] + 1
celkovy_pocet = sum(vyskyt_slov.values())
print(f"There are {celkovy_pocet} words in the selected text.")

titlecase_vypis = list()
titlecase_pocet = dict()

for slovo in vycistena_slova:
    if slovo.istitle():
        titlecase_vypis.append(slovo)

for slovo in titlecase_vypis:
    if slovo not in titlecase_pocet:
        titlecase_pocet[slovo] = 1
    else:
        titlecase_pocet[slovo] = titlecase_pocet[slovo] + 1
titlecase_sum = sum(titlecase_pocet.values())
print(f"There are {titlecase_sum} titlecase words.")

uppercase_vypis = list()
uppercase_pocet = dict()

for slovo in vycistena_slova:
    if slovo.isupper():
        uppercase_vypis.append(slovo)

for slovo in uppercase_vypis:
    if slovo not in uppercase_pocet:
        uppercase_pocet[slovo] = 1
    else:
        uppercase_pocet[slovo] = uppercase_pocet[slovo] + 1
uppercase_sum = sum(uppercase_pocet.values())
print(f"There are {uppercase_sum} uppercase words.")

lowercase_vypis = list()
lowercase_pocet = dict()

for slovo in vycistena_slova:
    if slovo.islower():
        lowercase_vypis.append(slovo)

for slovo in lowercase_vypis:
    if slovo not in lowercase_pocet:
        lowercase_pocet[slovo] = 1
    else:
        lowercase_pocet[slovo] = lowercase_pocet[slovo] + 1
lowercase_sum = sum(lowercase_pocet.values())
print(f"There are {lowercase_sum} lowercase words.")

numeric_vypis = list()
numeric_pocet = dict()

for slovo in vycistena_slova:
    if slovo.isnumeric():
        numeric_vypis.append(int(slovo))

for slovo in numeric_vypis:
    if slovo not in numeric_pocet:
        numeric_pocet[slovo] = 1
    else:
        numeric_pocet[slovo] = numeric_pocet[slovo] + 1
numeric_sum = sum(numeric_pocet.values())
print(f"There are {numeric_sum} numeric strings.")
numeric_total = sum(numeric_vypis)
print(f"The sum of all the numbers {numeric_total}")
print(oddelovac)

znaky_pocet = dict()
for pocet_znaku in vycistena_slova:
    pocet_znaku = len(pocet_znaku)
    if pocet_znaku not in znaky_pocet:
        znaky_pocet[pocet_znaku] = 1
    else:
        znaky_pocet[pocet_znaku] = znaky_pocet[pocet_znaku] + 1

print("LEN|    OCCURENCES    |NR.")
print(oddelovac)
znaky_pocet_sort = OrderedDict(sorted(znaky_pocet.items()))
for a, b in znaky_pocet_sort.items():
    hvezdicky = int(b) * "*"
    print(f"{a:>2} |{hvezdicky:<17} |{b:>3}")


