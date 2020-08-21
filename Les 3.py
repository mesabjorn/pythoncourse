# %% 
#les 3

# definieer een klasse met de naam Boek
class Boek():
    # eigenschappen van de klasse
    title = ""
    author = ""
    isbn = ""
    country_of_origin = "" 

    publication_year = -1
    page_count = -1

    # constructor, start bij aanmaak nieuwe instantie van klasse
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # de ingebouwde string functie moet een string teruggeven met wat je wilt laten zien van de klasse
    def __str__(self):
        return f"{self.author} - {self.title}"

# definieer een nieuwe instantie in variabele B van type Boek
B = Boek("Herman Melville","Moby Dick")
B.isbn = "0000-0000-0000"
B.country_of_origin = "London (UK)"
B.page_count = 635
B.summary = "Dit is een samenvatting van Moby Dick"
dir(B)              # lists all attributes and functions of an object

# %%

# lees de 500 books csv file in

f = open("./data/500_books.csv","r",encoding='utf-8')
l = f.readline()            # leest de header van de file (regel 1)

boekenkast = []             # definieer een lijst voor alle boeken

while(1):                                   # voor altijd (gelijk aan while(True) of while(1==1))
    try: 
        l = f.readline()                    # lees volgende regel in
        datarow = l.split(",")              # splits tekst op de komma's

        title = datarow[1]                  # haal titel uit kolom 2 (index 1)
        author = datarow[2]                 # haal auteur uit kolom 3 (index 2)

        B = Boek(author,title)              # maak nieuwe instantie van type Boek
        B.publication_year = datarow[10]    # haal jaartak uit kolom 11 (index 10)
        B.page_count = int(datarow[7])      # haal pagina's uit kolom 8 (index 7) en maak er een getal van met int()

        boekenkast.append(B)                # voeg boek B toe aan de lijst boekenkast
    except Exception as e:
        print(e)
        break

f.close()                                   # sluit file af


# bereken gemiddelde pagina's
all_pages = []
for b in boekenkast:
    all_pages.append(b.page_count)

gemiddeld_aantal_paginas = sum(all_pages)/len(all_pages)


# of korter en meer pythonesque
all_pages = (b.page_count for b in boekenkast)
gemiddeld_aantal_paginas = sum(all_pages)/len(boekenkast)

print(f"{len(boekenkast)} boeken ingeladen met een gemiddeld aantal pagina's van: {int(gemiddeld_aantal_paginas)}.")
