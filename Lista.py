import random
from operator import is_not
from unittest import removeResult

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

a = 2
b = 3

print (a <= b)
print (a >= b)
print (a == b)

sprawdź czy podane liczby są parzyste czy nieparzyste?

a = 5
b = 8
c = 13
d = 14

x = "Liczba Nieparzysta"
y = "Liczba Parzysta"

if a % 2 == 0:
    print(y)
else:
    print(x)

if b % 2 == 0:
    print(y)
else:
    print(x)

if c % 2 == 0:
    print(y)
else:
    print(x)

if d % 2 == 0:
    print(y)
else:
    print(x)

numbers = [1, 3, 6, 10]
for x in numbers:
    if x % 2 == 0:
        print (f"{x} - parzysta")
    else:
        print(f"{x} - nieparzysta")