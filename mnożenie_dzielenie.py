# | Operacja              | Symbol / Funkcja | Wynik             |
# | --------------------- | ---------------- | ----------------- |
# | Dzielenie z resztą    | `/`              | 10 / 3 = 3.333... |
# | Dzielenie bez reszty  | `//`             | 10 // 3 = 3       |
# | Reszta z dzielenia    | `%`              | 10 % 3 = 1        |
# | Iloraz i reszta razem | `divmod(a, b)`   | (3, 1)            |



import random
from colorama import Fore, Back, Style


print (Fore.LIGHTBLUE_EX + 'Witaj w programie tabliczka mnożenia')
print(Style.RESET_ALL)
punkty = 0

for i in range (10):

    a = random.randint (1, 10)
    b = random.randint (1, 10)

    wynik = input('Podaj wynik mnożenia '+str(a)+ '*' +str(b)+'= ')
    if int(wynik) == a*b:
        punkty = punkty+1
        print (Fore.LIGHTYELLOW_EX + 'świetnie Amelka. Doskonała odpowiedź :)')
        print(Style.RESET_ALL)
    else:
        print (Fore.RED + 'Niestety Źle Amelka, Ćwicz Dalej :(')
        print(Style.RESET_ALL)

print (Fore.LIGHTGREEN_EX + 'Odpowiedziałaś ' +str(punkty)+ ' razy dobrze. Otrzymujesz Lody ')
print(Style.RESET_ALL)


#---------------------------------------------------------------------------------

import random
from colorama import Fore, Style, init

# Inicjalizacja colorama
init(autoreset=True)

print(Fore.LIGHTBLUE_EX + '\nWitaj w programie tabliczka dzielenia!')
print(Style.RESET_ALL)
punkty = 0

for i in range(10):
    # Losuj liczby tak, żeby a dzieliło się przez b bez reszty
    b = random.randint(1, 10)
    # a musi być wielokrotnością b (czyli np. 10, 20, 30 dla b = 10)
    a = b * random.randint(1, 10)

    while True:
        wynik = input(f'Podaj wynik dzielenia {a} ÷ {b} = ')
        if wynik.isdigit():
            wynik = int(wynik)
            break
        else:
            print(Fore.YELLOW + 'Proszę wpisać liczbę!')

    if wynik == a // b:
        punkty += 1
        print(Fore.LIGHTYELLOW_EX + 'Świetnie Amelka! Doskonała odpowiedź :)')
    else:
        print(Fore.RED + f'Niestety źle. Poprawny wynik to {a // b}. Ćwicz dalej! :(')

print(Style.BRIGHT + f'\nOdpowiedziałaś {punkty} razy dobrze.')

if punkty == 10:
    print(Fore.LIGHTGREEN_EX + 'Perfekcyjnie! 🏆 Otrzymujesz DUŻE lody! 🍦')
elif punkty > 0:
    print(Fore.LIGHTGREEN_EX + 'Nieźle! Otrzymujesz małe lody 🍧')
else:
    print(Fore.YELLOW + 'Nie martw się! Następnym razem pójdzie lepiej 💪')
