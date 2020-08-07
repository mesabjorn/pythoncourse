# les 2
#
# a=10
# b=10
#
#
# if a==b:
# 	print("a is gelijk aan b")
# elif a > b:
# 	print("a is groter dan b")
# else:
# 	print("a is kleiner dan b")
#
#
# if type(a) == int and a > 5:
# 	print("a is een getal (integer) en groter dan 5.")
#
#
# for i in range(1,10):
#     print(i) 				# print de getallen van 1 t/m 9
#
#
# l = ["apple", "banana", "pear"]
# for f in l:
#     print(f)
#
#
# l = (0,10,100)
#
# for getal in l:
#     print(getal+2)
#
#
# i=0
# while i<10:
#     print(i) 				# print de getallen van 1 t/m 9
#     i += 1                  # hoog i met één op, korte notatie

naam = input("Wat is je naam?")
print(f"Hallo {naam}")

lft = input("Hoe oud ben je in jaren?")

lft_int = int(lft)

print(f"Dan ben je {lft_int*365} dagen op Aarde")
