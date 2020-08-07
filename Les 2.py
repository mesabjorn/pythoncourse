# les 2

# ------------------------------------------------------
# -----------------IF/ELIF/ELSE-------------------------
# ------------------------------------------------------
# if else statements checken of iets waar is: 0 of 1
# 0 is false oftewel, voer blok code niet uit
# 1 is true oftewel, voer codeblok wel uit

a = 10
b = 10

if a == b:                          # a is exact gelijk aan b
    print("a is gelijk aan b")
elif a > b:
    print("a is groter dan b")      # a is groter dan b
else:
    print("a is kleiner dan b")     # zo niet dan moet a dus kleiner zijn dan b

# er wordt dus elke keer als het script loopt, één regel uitgevoerd omdat die aan de vereisten voldoet, de
# rest wordt overgeslagen

# combineer statements met 'and' (beide waar), en 'or', minimaal één van twee waar
if type(a) == int and a > 5:                            # als a een getal is EN groter dan 5
    print("a is een getal (integer) en groter dan 5.")

if a > 5 or a == 2:                            # als a groter is dan 5, of gelijk is aan 2
    print("a is groter dan 5 of is gelijk aan 2")

# ------------------------------------------------------
# -----------------FOR - LOOPS--------------------------
# ------------------------------------------------------

# for loops voeren een regel binnen hun blok, een bekend aantal keer uit
# vb: deze for loop, print 9 keer een regel met het getal i
# notitie: de functie range() geeft een reeks getallen terug, in dit geval tussen 1 en 10 dus tm 9
for i in range(1, 10):
    print(i) 				# print de getallen van 1 t/m 9

# vb: deze for loop, print alle elementen in lijst l
l = ["apple", "banana", "pear"]
for f in l:
    print(f)

# vb: deze for loop, telt 2 op bij alle elementen in lijst l
l = [0, 10, 100]

for getal in l:
    print(getal+2)

# ------------------------------------------------------
# -----------------WHILE - LOOPS------------------------
# ------------------------------------------------------

# while loops voeren een taak uit zolang een bepaalde eis voldoet
# voorbeeld, zolang i onder de 10 is wordt het getal i geprint
# daarna stop de loop en wordt eventuele andere code uitgevoerd
i = 0                       # i moet gedefinieerd worden voor gebruik
while i < 10:               # zolang i onder de 10 is
    print(i) 				# print de getallen van 1 t/m 9
    i += 1                  # hoog i met één op, korte notatie,  anders zou deze loop nooit stoppen
                            # en i altijd 0 blijven. (Lange notatie is i = i+1
print("deze code staat buiten de while loop!")

# ------------------------------------------------------
# -----------------USER INPUT---------------------------
# ------------------------------------------------------

# de input() functie geeft de gebruiker mogelijkheden om data in te voeren
naam = input("Wat is je naam?")             # vraagt gebruiker om hun naam
print(f"Hallo {naam}")                      # begroet de persoon met zijn naam

lft = input("Hoe oud ben je in jaren?")     # vraagt gebruiker om zijn leeftijd

lft_int = int(lft)                          # input geeft string data terug, dus die moet omgezet worden naar een getal
                                            # staat ook bekend als parsing, of casting.

print(f"Dan ben je {lft_int*365} dagen op Aarde.")      # print het aantal dagen dat iemand leeft.
