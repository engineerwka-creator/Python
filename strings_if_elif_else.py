#---------------------------------------------------------------

imie = 'Karol'
wiek = 20

print ('Cześć mam na imię ',imie, 'i mam', wiek, 'lat')

kot = 'Mruczek'
print (f'Mam kota o imieniu', kot,)

kot = 'Mruczek'
print (f'Mam kota o imieniu {kot}')

#„Mam kota o imieniu Mruczek, który ma 3 lata”

cat = 'Mruczek'
age = 3
print (f'Mam kota o imieniu {cat},który ma {age} lata')

name = input ('Podaj imie?')
age = int (input ('podaj wiek?'))
print (f'Mam na imie {name} i mam {age + 5} lat')

#------------------------------------------------------------

#Get Numbers of pins

def get_number_of_pin (connector_name):
    if connector_name == "Phoenix":
        return 12
    elif connector_name == "d_sub":
        return 9
    else:
        return 0

age = int (input ('podaj wiek?'))
if age >= 18:
    print ('Pełnoletnia Osoba')
else:
    print ('Niepełnoletnia osoba')


print ("Ile  masz lat?")
wiek = int(input())
if wiek < 18:
    print("Nie można sprzedać alkoholu")
elif wiek == 18:
    print("Można sprzedać alkohol")
else:
    print("Zapytać o legitymację")

x = 3
y = 3
iloczyn = x*y
print("iloczyn: " +str(iloczyn))
if y == 0:
    print("Nie można dzielić przez zero")
else:
    iloraz = x/y
    print("iloraz: " +str(iloraz))
    modulo = x%y
    print("modulo: " +str(modulo))

x = ["apple", "banana"]
if "gruszka" not in x:
    print ("Nie ma gruszki")

print ("apple" in x)

#------------------------------------------------------------

#sprawdź czy podane liczby są parzyste czy nieparzyste?

a = 5
b = 8
c = 13
d = 14

x = "Liczba Nieparzysta"
y = "Liczba Parzysta"

if a % 2 == 0:
    print(y)
else:
    print(x)

if b % 2 == 0:
    print(y)
else:
    print(x)

if c % 2 == 0:
    print(y)
else:
    print(x)

if d % 2 == 0:
    print(y)
else:
    print(x)

numbers = [1, 3, 6, 10]
for x in numbers:
    if x % 2 == 0:
        print (f"{x} - parzysta")
    else: