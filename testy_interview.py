#Python: What kind of loop we have? Write the code how to use it them? (for, while)

for x in range (1, 6):
    print (x)

x = 1
while x < 6:
    print (x)
    x = x + 1

#Pętla for - liczby parzyste od 2 do 10.

print("Pętla for – liczby parzyste od 2 do 10:")
for i in range (2, 11, 2):
    print (i)

#Pętla for - liczby nieparzyste od 1 do 10.

print("Pętla for – liczby nieparzyste od 2 do 10:")
for i in range (1, 11, 2):
    print (i)


#przefiltruj liczby większe niż 10.

lista = [5, 16, 7, 12, 3, 19, 20, 43]

print ("Liczby większe niż 10:")
for i in lista:
    if i > 10:
        print (i)

wynik = [x for x in lista if x > 10]
print ("Liczby większe niż 10:", wynik)

#Regarding the “List”, write a code to show the list with 1, 3, 5?

list = [1, 3, 5]

print ("Oto nasza lista:")
print (list)

#wypisz wszystkie imiona w których występuje litera i

imiona = ["Adam", "Marek", "Irek", "Kasia", "Lilu", "Miki"]

print ("W tym imieniu występuje litera i:")
for y in imiona:
    if "i" in y.lower():
        print (y)

w = 2

while w in range (1,11):
    print (w)
    w = w + 2

#zadanie ze słownikiem

oceny = {
    "Ania": 5,
    "Marek": 3,
    "Iza": 2,
    "Kamil": 4,
    "Monika": 6
}

print ("Uczniowie z oceną 4 i wyższą:")
for uczen, ocena in oceny.items():
    if ocena >= 4:
        print (f"{uczen}: {ocena}")

auto = {
    "Ford": 1985,
    "Opel": 2023,
    "Fiat": 1982,
    "Toyota": 2004,
    "MAN": 1966
}

print ("Auta starsze niż 2004 rok:")
for old_cars, rocznik in auto.items():
    if rocznik < 2004:
        print (old_cars)


#przypisz stolicę do państwa
kraje = {
    "Polska": "Warszawa",
    "Francja": "Paryż",
    "Niemcy": "Berlin",
    "Włochy": "Rzym",
    "Hiszpania": "Madryt"
}


print ("Lista krajów i ich stolic:")
for kraj, stolica in kraje.items():
    print (f"{kraj} - {stolica}")

#Eliminacje do Mistrzostw świata

kraje = {
    "Polska": 2, "Finlandia": 1,
    "Francja": 4, "Belgia": 3,
    "Niemcy": 5, "Ukraina": 1,
    "Włochy": 3, "Holandia": 3,
    "Hiszpania": 5, "Portugalia": 4
}

print ("Wyniki wszystkich krajów w rozegranych meczach:")
isnewline = False
for kraj, wynik in kraje.items():
    endline = " "
    if isnewline == True:
        endline = "\n"
    print (f" {kraj} - {wynik}", end = endline)
    isnewline = not isnewline
