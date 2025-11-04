class Person:
    def __init__(self, name, age):
        # atrybuty instancji (stan)
        self.name = name
        self.age = age

    def greet(self):              # metoda — zachowanie
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# użycie


p = Person("Alicja", 30)
print(p.greet())  # Hi, I'm Alicja and I'm 30 years old.

#----------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def greet(self):  # metoda — zachowanie
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    # użycie


p1 = Person("Alicja", 30)
p2 = Person("Maja", 23)
p3 = Person("Kala", 18)

print(p1.greet())
print(p2.greet())
print(p3.greet())

#----------------------------------------------------------------

class Cable:
    def __init__(self, con_type_1, con_type_2, con_straight_1, con_angled_2, wire_type, length):

        self.con_type_1 = con_type_1
        self.con_type_2 = con_type_2
        self.con_straight_1 = con_straight_1
        #self.con_straight_2 = con_straight_2
        #self.con_angled_1 = con_angled_1
        self.con_angled_2 = con_angled_2
        #self.con_none_2 = con_none_2
        self.wire_type = wire_type
        self.length = length

    def choice(self):
        return f'Great Choice! You wish the cable with parameters: {self.con_type_1}, {self.con_type_2}, {self.con_straight_1}, {self.con_angled_2}, {self.wire_type}, {self.length}'

c1 = Cable( con_type_1= 'SMA', con_type_2= 'SMB', con_straight_1= 'straight', con_angled_2= 'angled', wire_type= 'RG174', length= '6 m.')

print(c1.choice())

#----------------------------------------------------------------

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

#computer - Metoda.
    def computer(self):
        return f"Great choice! You picked {self.brand} which costs {self.price} PLN."

# słownik z danymi
parametry = {'DELL': 3200, 'MAC': 8000, 'HP': 2700}


# funkcja wyboru
def choice():
    print("Dostępne laptopy:")
    for brand, price in parametry.items():
        print(f"- {brand}: {price} PLN")

    wybor = input("Wybierz laptop: ").upper()

    if wybor in parametry:
        cena = parametry[wybor]
        return Laptop(brand=wybor, price=cena)
    else:
        print("Nie ma takiego modelu.")
        return None


# program główny
l1 = choice() #tworzę obiekt klasy laptop i to mi zwraca L1 = choice()

if l1:
    print(l1.computer())

#----------------------------------------------------------------
VAT_rate = 0.23

class Kalkulator_Cen:
    def __init__(self, item, base_price):

        self.item = item
        self.base_price = base_price

    def gross_price (self):
       return 'Cena Brutto za {self.item} wynosi', self.base_price * 1+VAT_rate

I1 = Kalkulator_Cen (item= 'Pen_drive', base_price= 17)

print(I1.gross_price())

#-----------------------------------------------------------------
