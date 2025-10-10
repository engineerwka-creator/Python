#wypisz cyfry od 1 do 6 z użyciem pętli for.

for i in range(1, 7):
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
