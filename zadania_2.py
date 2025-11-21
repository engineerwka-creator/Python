
w2 = []
w3 = []

# tworzymy wielokrotności 2 jako 2^n
i = 1
while 2**i <= 50:
    w2.append(2**i)
    i += 1

# tworzymy wielokrotności 3 jako 3^n
j = 1
while 3**j <= 50:
    w3.append(3**j)
    j += 1

for liczba in range(1, 51):
    if liczba in w2 and liczba in w3:
        print("fuzzbuzz")
    elif liczba in w2:
        print("fuzz")
    elif liczba in w3:
        print("buzz")
    else:
        print(liczba)

p3 = []
p4 = []

a = 1
while 3**a <=50:
    p3.append(3**a)
    a +=1
b = 1

while 2**b <=50:
    p4.append(2**b)
    b +=1

for liczby in range(1,51):
    if liczby in p3 and p4:
        print ('SzkaLaka')
    elif liczby in p3:
        print ('Szaka')
    elif liczby in p4:
        print ('Laka')
    else:
        print (liczby)

#Wypisz Fuzz gdy liczba podzielna przez 2 oraz Buzz gdy liczba podzielna przez 3 w zakresie od 1 50. Pozostałe liczby również wypisz.
for liczba in range(1,51):
    if liczba % 2 == 0:
        print ('Fuzz')
    elif liczba % 3 == 0:
        print('Buzz')
    else:
        print (liczba)


from collections import Counter
from idlelib.iomenu import encoding

#------------------------------------------------------------------------
#Znajdź i policz unikalny znak taki jak wykrzyknik.
a = 'fashgfhasgf27165341265468!@#$$%^!!!!!!!!&*()*)_+_))'
print ('Znalazłem wykrzykników: ', a.count('!'))

#-----------------------------------------------------------------------
#Wypisza wskazane ilości literek z tej postaci '4a6b3c'

x = '4a6b3c'

pop_literka = ['a', 'z' in x]
pop_cyferka = ['1', '10' in x]

# for literka in x:
#     if literka == (pop_literka) * (pop_cyferka):
#         print (literka)


z = '2a5b9c'

znaki = ''
poprzedni_znak = ''

for liter_a in z:
    if liter_a.isalpha():
        poprzedni_znak = liter_a
    elif liter_a.isdigit():
        znaki += poprzedni_znak * int(liter_a)

print(znaki)

#--------------------------------------------------------------
#Jeśli wskazany element np. '#' występuje w krotce wyświetl Mamy '#' w krotce

u = (1,4,5,'f3h#')
for k in u:
    if '#' in str (u):
        print ('Mamy # w krotce')
        break

t = [1,4,5,'f3h#']

for f in t:
    if 5 in t:
        print ('Mamy t na liście')
        break

#-----------------------------------------------------------------
#Porównaj dwie listy. Jeśli takie same to True, jeśli nie to False.
a = [1,2,3,4],['qwerty']
b = [1,2,3,0],['qwerty']

print (a==b)

from collections import Counter

e = [1, 2, 2, 3]
f = [2, 3, 2, 1]

print(Counter(e) == Counter(f))


c = [1,2,3,4,5]
d = [5,6,7,8,9]

if set (c) & set (d):
    print ('karate')

wspolne = set(c) & set(d)
print("Wspólne elementy:", wspolne)

g = '12345'
h = '06789'

if any (x in g for x in h):
    print ('luksus')
else:
    print ('Nie ma takiego numeru :)')

i = ['M','K','L','O', 'V']
j = ['S','D','F','R','V']

wspolny = set(i) & set(j)
print ('wspolny element w zbiorach i oraz j, to: ', wspolny)

#-----------------------------------------------------------------------
#Napisz funkcję która bierze argumenty z list i zwraca True jeśli chodź jeden argument jest wspolny. W przeciwnym razie False.

# Test data for True:

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

if any(x in a for x in b):
    print('mamy coś')
    print(True)
else:
    print (False)

cos = set(a) & set(b)
print ('To coś to:', cos)

# Test data for False:

a =[1, 2, 3, 4, 5, 'Arek']
b =[6, 7, 8, 9, 0, 'Marek']

print (a == b)

if any(set(a) & set(b)):
    print ('Mamy jakiś wspolny elemnt')

    jakis_wspolny_el = (set(a) & set(b))
    print ('jakiś wspolny to: ', jakis_wspolny_el)

else:
    print ('Fuck you',False)
#--------------------------------------------------------------------------------------------

n = '4r67hj98kkv567h8k890'
liczby = ''
litery = ''

for digit in n:
    if digit.isdigit():
        liczby += digit
print (liczby)

for char in n:
    if char.isalpha():
        litery += char
print (litery)

#----------------------------------------------------------------------------------------------------

"""Write a function, that takes two lists as arguments, and returns True if at least one element is common between them. False otherwise."""
from charset_normalizer.cd import alpha_unicode_split

# Test data for True:

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

# Test data for False:

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]

def element_wspolny(a, b):
    for digit in a:
        if digit in b:
            return True
print ('Mamy wspólny element')
# return False

#-------------------------------------------------------
def element_wspolny(a, b):
    for digit in a:
        if digit in b:
            print('Mamy wspólny element')
            return True
    print('Brak wspólnego elementu')
    return False

# Testy
a = [1, 2, 3, 4, 5]
b = [10, 6, 7, 8, 9]
element_wspolny(a, b)

#-----------------------------------------------------------

x = {1,2,3,4,5}
y = {5,6,7,8,9}

x = {1,2,3,4,5}
y = {6,7,8,9}

def wspolny(x,y):
    for digit in x:
        if digit in y:
            return True
print ('Smile')

#-----------------------------------------------------------

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

if set(a) & set(b):  # operator & zwraca część wspólną zbiorów
    print("Mamy wspólny element")
else:
    print("Brak wspólnego elementu")


wspolne = list (set(a) & set(b))

if wspolne:
    print ('Mamy wspolny elemnt', wspolne)
#---------------------------------------------------------

example_list = [1,5,3,90,-1,12,7,3]
example_list.sort()

print (example_list)
#---------------------------------------------------------

example_l = [1,1,5,5,3,3,9,-1,12,7,3]

example_set = list (set(example_l))

print (example_set)

#-----------------------------------------------------------

w = '4d3w8k6g'

for char in w:
    if char.isalpha():
        print (char)
for digit in w:
    if digit.isdigit():
        print (digit)
#----------------------------------------------------------

w = '4d3w5k6g7x8v9q'
wynik = ''
poprzednia_litera = ''

for char in w:
    if char.isalpha():
        poprzednia_litera = char   # zapisujemy literę
    elif char.isdigit():
        wynik += poprzednia_litera * int(char)  # powtarzamy poprzednią literę

print(wynik)
#-----------------------------------------------------------------------------------
import os

if os.path.exists ('plik.txt'):
    print ('plik istnieje')

with open("plik.txt", "w", encoding="utf-8") as f:
    f.write ('\nPierwsza Linia ERROR')
    f.write ('\nDruga Linia ERROR, ERROR, ERROR\n')
    f.write ('Trzecia Linia ERROR\n')

with open ('plik.txt', 'r', encoding='utf-8') as f:
    licznik = sum(1 for _ in f)
    print ('Mamy w pliku lini  :',licznik)

policz = 'ERROR'
with open ('plik.txt', 'r', encoding='utf-8') as f:
    licz = sum(1 for l in f if policz in l)
    print ('Znalzłem',licz,'Błędy!')

with open ('plik.txt', 'r', encoding='utf-8') as f:
    log = f.read()
    lol = log.count('ERROR')

    print ('I found Numbers of the Errors:', lol)

lista = ['Ala', 'Kot', 'Jadzia','Jajo']

with open('plik.txt','w', encoding='utf=8') as f:
    f.write (' '.join(lista)) #dodaje do pliku listę lub co chcesz :)

with open ('plik.txt','r',encoding='utf-8') as f:
    for linia in f:
        print (linia)

with open("plik.txt", "r", encoding="utf-8") as f:
    zawartosc = f.read()
print(zawartosc)

with open ('dane.json', 'w') as f: #tworzenie nowego pliku
    pass
#---------------------------------------------------------------------------------------
def policz_logi():
    """
    Funkcja wczytuje plik 'Logs' z podanej lokalizacji i zlicza
    ilość wystąpień ERROR, WARNING, INFO.
    """

    sciezka = r"c:\Python_Projects\PycharmProjects\Python\Logs.txt"

    wyniki = {
        "ERROR": 0,
        "WARN": 0,
        "INFO": 0
    }

    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            for linia in f:
                for key in wyniki:
                    if key in linia:
                        wyniki[key] += 1
        return wyniki

    except FileNotFoundError:
        print(f"Plik {sciezka} nie istnieje!")
        return None


# użycie:
statystyki = policz_logi()
if statystyki:
    print("Statystyki logów:", statystyki)

#--------------------------------------------------------------------------------------------
#
# def policz_miesiące():
#
#
#         path = (r"c:\Python_Projects\PycharmProjects\Python\months.txt")
#
#         total = {'styczeń': 0,
#                  'luty': 0,
#                 'marzec': 0,
#                  'kwiecień': 0,
#                  'maj': 0,
#                  'czerwiec': 0,
#                  'lipiec': 0,
#                  'sierpień': 0,
#                  'wrzesień': 0,
#                  'październik': 0,
#                  'listopad': 0,
#                  'grudzień': 0}
#
#         with open (path, 'r', encoding='utf-8') as f:
#                 for line in f:
#                     for key in total:
#                         if key in line:
#                             total[key] += 1
#         return total
#
#
#
# print ('Mamy miesiące w ilości:', '\n', policz_miesiące())

#----------------------------------------------------------------------

def policz_wartości():

    path = (r"c:\Python_Projects\PycharmProjects\Python\months.txt")

    total = {}

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            month, value = line.split()
            value = float (value)
            total[month] += value
        return total

wyniki = policz_wartości()

print ('Mamy w sumie wartości:', '\n', wyniki)

