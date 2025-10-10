import random

# Lista przykładowych imion i nazwisk
imiona = ["Jan", "Anna", "Piotr", "Maria", "Krzysztof", "Julia", "Tomasz", "Alicja"]
nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Dąbrowski", "Lewandowski", "Wójcik", "Kamiński", "Zieliński"]

# Lista przedmiotów szkolnych
przedmioty = ["Matematyka", "Język polski", "Historia", "Biologia", "Fizyka", "Chemia", "Geografia", "Informatyka"]

# Funkcja generująca oceny dla ucznia
def generuj_oceny():
    return {przedmiot: random.randint(2, 6) for przedmiot in przedmioty}

# Funkcja generująca uczniów i ich oceny
def generuj_uczniow(liczba_uczniow):
    uczniowie = []
    for _ in range(liczba_uczniow):
        imie = random.choice(imiona)
        nazwisko = random.choice(nazwiska)
        oceny = generuj_oceny()
        uczniowie.append({"Imię": imie, "Nazwisko": nazwisko, "Oceny": oceny})
    return uczniowie

# Generowanie i wyświetlanie informacji o uczniach
liczba_uczniow = 5  # Można zmienić na dowolną wartość
uczniowie = generuj_uczniow(liczba_uczniow)

for uczen in uczniowie:
    print(f"{uczen['Imię']} {uczen['Nazwisko']}")
    for przedmiot, ocena in uczen["Oceny"].items():
        print(f"  {przedmiot}: {ocena}")
    print()