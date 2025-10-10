#total mod 11 == 0

def validate_ISBN (ISBN):
    total = 0
    index = 10
    for znak in ISBN:
        if znak.isdigit():
            total = total + int(znak) * index
            index -= 1
        if znak == 'X':
            total = total + 10 * index
            index -= 1
    return total % 11 == 0
wynik = validate_ISBN ("3-598-21507-X")
print (wynik)

moja_lista = ['jabłko', 'banan', 'gruszka']
for owoc in moja_lista:
    print(owoc)