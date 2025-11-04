
#-----------------------------------------------------------
# LISTA - Lista to kolekcja elementów, które można zmieniać (dodawać, usuwać, modyfikować). Ma kolejność i może zawierać różne typy danych.

owoce = ["jabłko", "banan", "gruszka"]

# Dodawanie elementu
owoce.append("truskawka")

# Dostęp do elementu (indeksy od 0)
print(owoce[0])   # jabłko

# Zmiana elementu
owoce[1] = "śliwka"

print(owoce)

#-----------------------------------------------------------
# KROTKA (TUPLE) - Krotka to lista, której nie można zmieniać — czyli jest niezmienna (immutable). Dobrze nadaje się do przechowywania stałych danych.

# Tworzenie krotki
kolory = ("czerwony", "zielony", "niebieski")

# Dostęp do elementu
print(kolory[1])  # zielony

# Próba zmiany spowoduje błąd:
# kolory[0] = "biały" ❌ (nie można!)

#-----------------------------------------------------------
# SŁOWNIK (DICT) - Słownik to zbiór par: klucz → wartość. Używasz go, gdy chcesz szybko znaleźć wartość po nazwie (kluczu).

# Tworzenie słownika
osoba = {
    "imię": "Amelka",
    "wiek": 10,
    "miasto": "Warszawa"
}

# Dostęp po kluczu
print(osoba["imię"])   # Amelka

# Dodawanie nowej pary
osoba["ulubiony_kolor"] = "różowy"

# Zmiana wartości
osoba["wiek"] = 11

print(osoba)

#-----------------------------------------------------------
# ZBIÓR(SET) - Zbiór to kolekcja unikalnych elementów — nie ma duplikatów i nie ma określonej kolejności.

# Tworzenie zbioru
liczby = {1, 2, 3, 3, 4, 4, 5}

print(liczby)  # duplikaty zostaną usunięte

# Dodawanie elementu
liczby.add(6)

# Usuwanie elementu
liczby.remove(3)

print(liczby)

#-----------------------------------------------------------

imiona = ["Karol", "Ala", "Pawel", "Kala", "Kasia", "Pola", "Maja", "Radek" ]

nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Dąbrowski", "Lewandowski", "Wójcik", "Kamiński", "Zieliński"]

przedmioty = ["Matematyka", "Język polski", "Historia", "Biologia", "Fizyka", "Chemia", "Geografia", "Informatyka"]

def generuj_oceny ():
    return {przedmiot: random.randint(a=2, b=6) for przedmiot in przedmioty}


#wypisz cyfry od 1 do 5.

def wypisz_liczby ():

    x = 5
    for x in range (1, 6):
        if x == 3:
            continue
        print (x)
wypisz_liczby ()

def wypisz_liczby2 ():
    x = 0
    while x < 5:
        x = x+1
        print(x)
wypisz_liczby2()

#jak przefiltrować tylko liczby większe niż 10 z listy

lista = [11, 6, 13, 17, 2, 14, 19]

def wieksze_niż_10 (lista):
    wynik = []
    for x in lista:
        if x > 10:
            wynik.append(x)
    return wynik
wynik = wieksze_niż_10 (lista)
print (wynik)

def count_chars(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    return counter


print(count_chars("tttttest"))
