import re
regex = r"^[Ff].*?[0-5].*?[Vv]$" #ime i prezime je: Frano Vrankjković
ime_prezime = input("Unesite ime i prezime: ")
if re.match(regex, ime_prezime):
    print("Podudaranje pronađeno!")
else:
    print("Nema podudaranja.")
