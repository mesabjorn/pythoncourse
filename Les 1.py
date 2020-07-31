# dit is een comment, deze regel wordt genegeerd

"""
dit
is een comment 
over meerdere regels
"""

print("Hello world") # gebruik de print functie om de tekst 'Hello world' naar het scherm te printen!

a = 5 # definieer een variabele met naam a en waarde 5
b = 3 # definieer een variabele met naam b en waarde 5

c = a*b # 15

print(f"a={a},b={b}, dus c=a*b={a}*{b}={c}")

# Lists, wijzigbare lijsten

print("Lists:")
print("\tDefinieer met rechte haken []")

l = ["a",1,-1, 3.2,True] # definieer een lijst met 5 elementen/objecten
len(l) # gebruik funcie 'len' om de lengte van een lijst te krijgen

print("\tl = ['a',1,-1, 3.2,True] # definieer een lijst met 5 elementen/objecten")
print(f"\tlijst heeft {len(l)} elementen\n\n") # print lengte van l naar scherm
l[0] # haal eerste element uit lijst op
l[1] # haal tweede element uit lijst op
l[-1] # haal laatste element uit lijst op

l[2] = 5 # op positie 3, vul waarde 5 in in de lijst l


# Tuples, onwijzigbare lijsten
print("Tuples:")
print("\tDefinieer met ronde haken ()")
print("\tt = ('a',1,-1, 3.2, True) # definieer een lijst met 5 elementen/objecten")
print(f"\tlijst heeft {len(l)} elementen\n\n") # print lengte van l naar scherm
t = ("a",1,-1, 3.2, True) # definieer een Tuple met 5 elementen/objecten
len(t) # gebruik funcie 'len' om de lengte van een Tuple te krijgen

print(f"\t{len(t)}") # print lengte van l naar scherm
l[0] # haal eerste element uit lijst op
l[1] # haal tweede element uit lijst op
l[-1] # haal laatste element uit lijst op


# Dictionary, key-value mapping
print("Dictionaries:")
print("\tDefinieer met accolades {}")

patient = {"Naam":"Piet","Leeftijd":40,"study_patient":True}
patient.get("Naam") # geeft Piet terug
patient["Naam"]		# geeft ook Piet terug
print(f"\tpatient = {patient}")

print("\n\n\nEen lijst met patienten uit een tekstfile:")


f = open("./data/patienten.csv")		# open tekstfile 'patients.csv'
regels = f.readlines()			# lijst van regels in tekstfile: 'patients.csv'
f.close()						# sluit file na gebruik

patients = []					# definieer een lege lijst

for regel in regels:	# loopt door lijst heen
	print("\t"+regel)		# elk object in de lijst wordt één voor één in de variabele regel geplaats
	data = regel.split(",")	# split de tekstdata op elke komma
	patient = {"id":data[0],"Naam":data[1],"Leeftijd":data[2],"bloeddruk":data[3]}
	patients.append(patient)	# voeg hier elke iteratie een patient aan toe
	
#print(patients)			# buiten for-loop, let op indentatie.

print("\n\nAlle bloeddrukken:")
print(list(map(lambda x: x["bloeddruk"].replace("\n",""),patients[1:])))

	
	





