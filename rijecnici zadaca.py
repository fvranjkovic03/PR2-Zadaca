import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
         'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
         'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
         'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
         'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

ocjene = {}

for ime in imena:
    ocjena = random.randint(1, 5)
    if ime in ocjene:
        ocjene[ime].append(ocjena)
    else:
        ocjene[ime] = [ocjena]

broj_ocjena = len(imena)
broj_prolaznih = 0
broj_neprolaznih = 0

for ime, lista_ocjena in ocjene.items():
    for ocjena in lista_ocjena:
        if ocjena > 1:
            broj_prolaznih += 1
        else:
            broj_neprolaznih+= 1

postotak_prolaznosti = (broj_prolaznih / broj_ocjena) * 100

print("Broj prolaznih ocjena:", broj_prolaznih)
print("Broj neprolaznih ocjena:", broj_neprolaznih)
print("Postotak prolaznosti: {:.2f}%".format(postotak_prolaznosti))
