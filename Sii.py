"""Write a function, that takes two lists as arguments, and returns True if at least one element is common between them. False otherwise."""
from charset_normalizer.cd import alpha_unicode_split

# Test data for True:

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

# Test data for False:

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]

def element_wspolny(a, b):
    for digit in a:
        if digit in b:
            return True
print ('Mamy wspólny element')
# return False

#-------------------------------------------------------
def element_wspolny(a, b):
    for digit in a:
        if digit in b:
            print('Mamy wspólny element')
            return True
    print('Brak wspólnego elementu')
    return False

# Testy
a = [1, 2, 3, 4, 5]
b = [10, 6, 7, 8, 9]
element_wspolny(a, b)

#-----------------------------------------------------------

x = {1,2,3,4,5}
y = {5,6,7,8,9}

x = {1,2,3,4,5}
y = {6,7,8,9}

def wspolny(x,y):
    for digit in x:
        if digit in y:
            return True
print ('Smile')

#-----------------------------------------------------------

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

if set(a) & set(b):  # operator & zwraca część wspólną zbiorów
    print("Mamy wspólny element")
else:
    print("Brak wspólnego elementu")


wspolne = list (set(a) & set(b))

if wspolne:
    print ('Mamy wspolny elemnt', wspolne)
#---------------------------------------------------------

example_list = [1,5,3,90,-1,12,7,3]
example_list.sort()

print (example_list)
#---------------------------------------------------------

example_l = [1,1,5,5,3,3,9,-1,12,7,3]

example_set = list (set(example_l))

print (example_set)

#-----------------------------------------------------------

w = '4d3w8k6g'

for char in w:
    if char.isalpha():
        print (char)
for digit in w:
    if digit.isdigit():
        print (digit)
#----------------------------------------------------------

w = '4d3w5k6g7x8v9q'
wynik = ''
poprzednia_litera = ''

for char in w:
    if char.isalpha():
        poprzednia_litera = char   # zapisujemy literę
    elif char.isdigit():
        wynik += poprzednia_litera * int(char)  # powtarzamy poprzednią literę

print(wynik)
