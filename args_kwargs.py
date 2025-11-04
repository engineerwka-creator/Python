#-------------------------------------------------------------
kwargs = {'name': 'Ala', 'age': 25, 'city': 'Warszawa'}

for (key, value) in kwargs.items():
    print(f"{key} = {value}")

#-------------------------------------------------------------
def show_all(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show_all(1, 2, "Python", name="Ola", level="beginner")

def add_all(*args):
    return sum (args)

print(add_all(1, 2, 3))       # 6
print(add_all(10, 20, 30, 40)) # 100

#-------------------------------------------------------------

def greet(name, age):
    print(f"Cześć {name}, masz {age} lat!")

args = ("Ola", 25)
kwargs = {"name": "Jan", "age": 30}

greet(*args)      # Cześć Ola, masz 25 lat!
greet(**kwargs)   # Cześć Jan, masz 30 lat!


#-------------------------------------------------------------

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

#-------------------------------------------------------------

def funkcja(test, *kot, **kwargs):
    print("test:", test)
    print("role:", kot)
    print("kwargs:", kwargs)

funkcja("start", 1, 2, 3, imie="Ada", wiek=30)

def suma(*args):
    print (args)
    print (sum(args))

suma (1, 3, 5, 7)

#-------------------------------------------------------------