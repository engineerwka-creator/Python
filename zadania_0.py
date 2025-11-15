#--------------------------------------------------------------------------------
# Napisz program, który po wczytaniu liczby naturalnej określającej wiek pewnej osoby sprawdzi, czy jest ona pełnoletnia.

def klient():
    wiek = int(input('Ile masz lat?  '))

    if 18 <= wiek <= 100:
        print ('Pełnoletni')
    elif 1 <= wiek < 18:
        print ('Niepełnoletni')

klient()
#--------------------------------------------------------------------------------
#Napisz program, który zamieni minuty na godziny i minuty.

def czas():
    godzina = (220//60)
    minuty = (220%60)
    print (str(godzina)+'h', str(minuty)+'min')

czas()
#lub
print(str(220//60)+'h',str(220%60)+'min')

#--------------------------------------------------------------------------------
#Napisz program, który po wczytaniu liczby całkowitej określającej temperaturę powietrza, określi czy jest ciepło, zimno czy gorąco.
#Zimno jest wtedy, gdy temperatura spadnie poniżej 17 stopni, ciepło jest w przedziale od 17 do 26 stopni, a gorąco jest powyżej 26 stopni.

def temp():
    t = float (input('Podaj temperaturę?  '))
    if 0 <= t < 17:
        print ('zimno')
    elif 17 < t < 26:
        print ('ciepło')
    else:
        print ('gorąco')

temp()

#--------------------------------------------------------------------------------
#Napisz program, który po wczytaniu cyfry, wypisze jej nazwę słownie.

def losuj():
    cyfra = int(input('podaj cyfrę  '))
    cyfra_tekst = {0:'zero', 1:'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'pięć', 6: 'sześć', 7: 'siedem', 8: 'osiem', 9: 'dziewięć'}
    print (cyfra_tekst.get (cyfra))

losuj()

#--------------------------------------------------------------------------------
