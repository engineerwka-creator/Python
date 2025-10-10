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
