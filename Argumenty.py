def suma(*args):
    print(args)
    return sum(args)

print(suma(1, 2, 3, 4, 5, 6))
print(suma(10, 20))

def przedstaw_sie(**kwargs):
    print(kwargs)
    for klucz, wartosc in kwargs.items():
        print(f"{klucz}: {wartosc}")

przedstaw_sie(imie="Ola", wiek=25, miasto="Kraków", miejsce_urodzenia="Wrocław")

def funkcja(test, *kot, **kwargs):
    print("test:", test)
    print("role:", kot)
    print("kwargs:", kwargs)

funkcja("start", 1, 2, 3, imie="Ada", wiek=30)

def suma(*args):
    print (args)
    print (sum(args))

suma (1, 3, 5, 7)

import time

def dekorator(funkcja):
    b = 10
    def nowa_funkcja():
        start = time.time()
        # print("Przed wywołaniem funkcji")
        funkcja ()
        # print("Karol", a, b)
        koniec = time.time()
        print(f"Czas wykonania: {koniec - start:.4f} sekundy")
        # print("Po wywołaniu funkcji")
    print ("funkcja_dekorator")
    return nowa_funkcja

def przyklad():
    print("Cześć!")

f = dekorator(przyklad)
print ("Jaga")\
f ()

def przyklad_2():
    time.sleep(2)
f = dekorator(przyklad_2)
print("Jaga")
f()

@dekorator
def test30():
    print("test_30")
    time.sleep(1)
test30()

@dekorator
def test31():
    print("test_31")
    time.sleep(1)
test31()