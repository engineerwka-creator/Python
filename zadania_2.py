# w2 = []
# w3 = []
#
# # tworzymy wielokrotności 2 jako 2^n
# i = 1
# while 2**i <= 50:
#     w2.append(2**i)
#     i += 1
#
# # tworzymy wielokrotności 3 jako 3^n
# j = 1
# while 3**j <= 50:
#     w3.append(3**j)
#     j += 1
#
# for liczba in range(1, 51):
#     if liczba in w2 and liczba in w3:
#         print("fuzzbuzz")
#     elif liczba in w2:
#         print("fuzz")
#     elif liczba in w3:
#         print("buzz")
#     else:
#         print(liczba)
#
# p3 = []
# p4 = []
#
# a = 1
# while 3**a <=50:
#     p3.append(3**a)
#     a +=1
# b = 1
#
# while 2**b <=50:
#     p4.append(2**b)
#     b +=1
#
# for liczby in range(1,51):
#     if liczby in p3 and p4:
#         print ('SzkaLaka')
#     elif liczby in p3:
#         print ('Szaka')
#     elif liczby in p4:
#         print ('Laka')
#     else:
#         print (liczby)
#
#Wypisz Fuzz gdy liczba podzielna przez 2 oraz Buzz gdy liczba podzielna przez 3 w zakresie od 1 50. Pozostałe liczby również wypisz.
# for liczba in range(1,51):
#     if liczba % 2 == 0:
#         print ('Fuzz')
#     elif liczba % 3 == 0:
#         print('Buzz')
#     else:
#         print (liczba)

#------------------------------------------------------------------------
#Znajdź i policz unikalny znak taki jak wykrzyknik.
# a = 'fashgfhasgf27165341265468!@#$$%^!!!!!!!!&*()*)_+_))'
# print ('Znalazłem wykrzykników: ', a.count('!'))

#-----------------------------------------------------------------------
# Wypisza wskazane ilości literek z tej postaci '4a6b3c'

# x = '4a6b3c'
#
# pop_literka = ['a', 'z' in x]
# pop_cyferka = ['1', '10' in x]
#
# for literka in x:
#     if literka == (pop_literka) * (pop_cyferka):
#         print (literka)


z = '2a5b9c'

znaki = ''
poprzedni_znak = ''

for liter_a in z:
    if liter_a.isalpha():
        poprzedni_znak = liter_a
    elif liter_a.isdigit():
        znaki += poprzedni_znak * int(liter_a)

print(znaki)