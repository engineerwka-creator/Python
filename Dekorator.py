
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

def log_decorator(func):
    def wrapper():
        print("➡️ Funkcja się zaraz wykona...")
        func()
        print("✅ Funkcja zakończyła działanie.")
    return wrapper

@log_decorator
def say_hello():
    print("Cześć!")

say_hello()
