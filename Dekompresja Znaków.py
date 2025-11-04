# def decompress_string(compressed_string):
#     decompressed_result = ""
#     count_str = ""
#     current_char = ""
#
#     for char in compressed_string:
#
#         if char.isdigit():
#             count_str += char
#
#         else:
#             if count_str:
#                 count = int(count_str)
#                 decompressed_result += current_char * count
#
#             current_char = char
#             count_str = ""
#
#     if count_str:
#         count = int(count_str)
#         decompressed_result += current_char * count
#
#     return decompressed_result
#
#
#
# import re
# tekst = 'a4b3r6'
#
# def dekompresja():
#
#     matches = re.findall(r'([a-zA-Z])(\d+)', tekst)
#
#     wynik = "".join(char * int(count) for char, count in matches)
#
#     return wynik
#
# zdekompresowany_tekst = dekompresja()
# print(zdekompresowany_tekst)
from test_Python_test import test_isosceles

tekst = 'a4b3r6'
wynik = ''
poprzedni_znak = ''


for znak in tekst:
    if 'a' <= znak <= 'z':
        poprzedni_znak = znak
    else:
        wynik = wynik + poprzedni_znak * int(znak)
print (wynik)

str_1 = 'test'
str_2 = 'piatek'
str_result = str_1 + str_2

str_result2 = ''
str_result2 += str_1
str_result2 += str_2

print (str_result)
print (str_result2)