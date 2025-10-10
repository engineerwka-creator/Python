# funkcja len podaje ilość znaków


x = len("12345abcdef")
print (x)

# funkcja 'input' oczekuję wprowadzenia danych

przedmiot1 = input("Ocena Metematyka - Podaj Imię ")
ocena1 = 5
print (ocena1)

przedmiot2 = input("Ocena J.Polski - Podaj Imię ")
ocena = ocena1 - 2
print (ocena)

import csv

# Dane do wyeksportowania
dane = [
    {'imie': 'Jan Kowalski', 'matematyka': 4, 'historia': 5},
    {'imie': 'Anna Nowak', 'matematyka': 5, 'historia': 4.5},
    {'imie': 'Piotr Wiśniewski', 'matematyka': 3, 'historia': 3}
]

# Nagłówki kolumn
naglowki = ['imie', 'matematyka', 'historia']

# Nazwa pliku do zapisu
nazwa_pliku = 'oceny.csv'

# Zapisywanie danych do pliku CSV
try:
    with open(nazwa_pliku, 'w', newline='', encoding='utf-8') as csv:
        writer = csv.DictWriter (csv, fieldnames=naglowki, delimiter=';')

        # Zapisanie nagłówka
        writer.writeheader()

        # Zapisanie danych
        writer.writerows(dane)

    print(f"Dane zostały pomyślnie zapisane do pliku '{nazwa_pliku}'.")

except IOError as e:
    print(f"Wystąpił błąd podczas zapisu do pliku: {e}")
open('oceny.csv', 'w', newline='', encoding='utf-8')