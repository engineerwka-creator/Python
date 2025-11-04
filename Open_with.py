licznik =  0
brak_Karol = 0

with open("c:\\Python_Projects\\Karol.txt", "r", encoding="utf-8") as f:
    for line in f:
        if 'Karol' in line:
            licznik = licznik +1
            print(line.rstrip("\n"))
        else:
            brak_Karol = brak_Karol +1

print (licznik)
print (brak_Karol)
print (licznik + brak_Karol)

#--------------------------------------------------------------------------

moj_zbior = set()
is_duplicated = False

with open("c:\\Python_Projects\\Karol2.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line in moj_zbior:
            is_duplicated = True
            break
        moj_zbior.add (line)

print (moj_zbior)
print (is_duplicated)

#--------------------------------------------------------------------------

moja_lista = list()

with open('c:\\Python_Projects\\Karol.txt', 'r', encoding='utf-8') as plik:
    for l in plik:
        moja_lista.append(l.strip() + ' Matrix')

print (moja_lista)

# Otwieramy plik źródłowy w trybie odczytu
with open('c:\\Python_Projects\\Karol2.txt', 'r', encoding='utf-8') as plik:
    linie = plik.readlines()

# Tworzymy listę z dopisanym słowem 'matrix' do każdej linii
nowe_linie = []
for l in linie:
    nowe_linie.append(l.strip() + ' matrix\n')

# Zapisujemy wynik do nowego pliku
with open('c:\\Python_Projects\\Karol2_matrix.txt', 'w', encoding='utf-8') as nowy_plik:
    nowy_plik.writelines(nowe_linie)

print("✅ Utworzono nowy plik: Karol2_matrix.txt z dopisanym słowem 'matrix'!")

-------------------------------------------------------------------------------
with open('c:\\Python_Projects\\Karol2.txt', 'r', encoding='utf-8') as plik:
    linie = plik.readlines()

nowe_linie = ()

# Iterujemy po liniach
for l in linie:
    tekst = l.strip()

# Jeśli linia zaczyna się na 'R', dodajemy 'matrix'
    if tekst.startswith('R'):
        nowe_linie.append(tekst + ' matrix\n')
    else:
        nowe_linie.append(tekst + '\n')

# Zapisujemy wynik do nowego pliku

with open('c:\\Python_Projects\\Karol2_matrix.txt', 'w', encoding='utf-8') as nowy_plik:
    nowy_plik.writelines(nowe_linie)

print("✅ Utworzono plik z dopisanym 'matrix' do linii zaczynających się na R.")

#-----------------------------------------------------------------------------------
import os

with open('c:\\Python_Projects\\Robot.xls', 'w', encoding='utf-8') as nowy_plik:
    nowy_plik.write ('Cześć jestem nowym plikiem o nazwie Robot')

sciezka = ('c:\\Python_Projects\\Robot.txt')

if os.path. exists(sciezka):
    os.remove (sciezka)
    print ('plik został usunięty')

else:
    print ('plik nie został znaleziony')

#-----------------------------------------------------------------------------------

with open('C:\\Users\\engin\\OneDrive\\Desktop\\Rozwój_Osobisty\\Wire Harnesses Engineer\\Kalkulacja.xlsx', 'r', encoding='utf-8') as file:
    for cela in file:
        if Wiazka in cela or Marża: