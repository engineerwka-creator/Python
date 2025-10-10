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