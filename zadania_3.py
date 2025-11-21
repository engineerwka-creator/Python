#--------------------------------------------------

imie = 'Karol'  #zmienna imie
wiek = 35       #zmienna wiek

print (imie, 'ma', wiek, 'lat')

wiek_za_15_lat = wiek + 15
print (imie, 'ma', wiek_za_15_lat, 'lat')
#-------------------------------------------------
cena_netto = 49.99
stawka_vat = 0.23

#Cena_Brutto = cena_netto * (1+stawka_vat)

print (int (cena_netto * (1+stawka_vat)))
cena_brutto = (cena_netto * (1+stawka_vat))

print (cena_brutto)

if cena_brutto > 100:
    print ('Drogi Produkt')
elif cena_brutto < 100:
    print('Tani Produkt')
else:
    print ('Produkt do Wyceny')

#print digits 1 to 5
for x in range (1,6):
    print (x)

for char in imie:
    print (char)
#-------------------------------------------

STAWKA_PROWIZJI = 0.05
cena_startowa = 100
numer_produktu = 1


for numer_produktu in range(3):
    cena_produktu = cena_startowa + (numer_produktu * 10)
    prowizja = (cena_produktu * STAWKA_PROWIZJI)

    print(f"Produkt numer {numer_produktu + 1}: Prowizja wynosi {prowizja} zł.")

STAWKA_PROWIZJI = 0.05
cena = 200

STAWKA_PROWIZJI = 0.05
cena = 200

def oblicz_prowizje(cena):
    wynik = cena * STAWKA_PROWIZJI
    print(wynik)

oblicz_prowizje(cena)

def przywitaj():
    print("Cześć!")
przywitaj()
#---------------------------------------
cena = 100
# print(cena * 0.05)

cena = 200
# print(cena * 0.05)

cena = 300
# print(cena * 0.05)

def oblicz_prowizje(cena):
    print(cena * 0.05)

oblicz_prowizje(100)
oblicz_prowizje(200)
oblicz_prowizje(300)
#--------------------------------------------

def przywitaj(imie):
    print (f'Cześć, {imie}!')

przywitaj('Karol')
przywitaj('Ala')

#---------------------------------------------

def reverse (text):
    result = ""
    for c in reversed(text):
        result += c
    return (result)
print (reverse("Karol")  )

def reverse2(text):
    return text[::-1]
print (reverse2("Karol"))

#------------------------------------------------
