#pętle - loops
for x in range(5):
    print (x)
#wypisz cyfry od 1 do 7 po kolei

oceny = [1, 2, 3, 4, 5, 6, 7]
for i in range (len (oceny)):
    print (oceny[i])

#wypisz cyfry od 1 do 5 z użyciem pętli while.
def wypisz_liczby2 ():
    x = 0
    while x < 5:
        x = x+1
        print(x)
wypisz_liczby2()

def wypisz_liczby2():
    for x in range(1, 6):
        print(x)


y = 0
while y < 7:
    print(y)
    y += 1

for a in range(5, 10):
    if a % 2 == 0:
        print ("Liczba jest parzysta: "+str (a))
    else:
    #a % 2 == 1:
        print("Liczba jest nie parzysta: "+str (a))
b = 30
x = 2
while x < 100:
    print("Liczba: x=", x, x, x, b, x*b, sep = "     ", end = "  Koniec LINI\n")
    x = x * x


counter = 0
for a in range(10, 100):
    if a % 10 == 0:
        counter += 1
print("counter =", counter)


for a in range(0, 10):
    if a % 2 == 0:
        print(f"The number {a} is even: True")
    else:
        print(f"The number {a} is even: False")

#wypisz cyfry od 1 do 5 z użyciem pętli for.

for i in range(1, 6):
    print(i)

#wypisz cyfry od 1 do 5 z użyciem pętli while.

i = 1
while i < 6:
    print(i)
    i = i + 1

#przefiltruj liczby większe niż 10 z listy

lista = [11, 6, 13, 17, 2, 14, 19]

def wieksze_niż_10 (lista):
    wynik = []
    for x in lista:
        if x > 10:
            wynik.append(x)
    return wynik
wynik = wieksze_niż_10 (lista)
print (wynik)

#sprawdź czy podane liczby są parzyste czy nieparzyste?
numbers = [1, 3, 6, 10]
for x in numbers:
    if x % 2 == 0:
        print (f"{x} - parzysta")
    else:
        print(f"{x} - nieparzysta")