#Ustawienia poczatkowe

przycisk_on = True       #silnik otwiera
przycisk_off = True     #silnik zamyka
czujnik_gora = True     #brama otwiera się
czujnik_dol = True     #brama zamyka się

#Funkcje i zachowanie silnika

def silnik_otworz():
    print ('Brama otwiera się')

def silnik_zamknij():
    print ('Brama zamyka się')

def silnik_stop():
    print ('Blad Spr. Brame i ponownie naciśnij Otwórz lub Zamknij')

przycisk_on = input('brama otwiera się? tak/nie   ').lower () == 'tak'
przycisk_off = input('brama zamyka się? tak/nie  ').lower () == 'tak'

#Warunki otwierania i zamykania bramy

if przycisk_on and czujnik_gora:
    silnik_otworz()

elif przycisk_off and czujnik_dol:
    silnik_zamknij()

else:
    silnik_stop()
