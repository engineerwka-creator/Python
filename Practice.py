# funkcja 'input' oczekuję wprowadzenia danych

stan_konta = input("Podaj stan konta ")
stan_konta = int (stan_konta)
stan_konta = stan_konta + 500*2
print (stan_konta)

FN = "Karol "
LN = "Wisniewski"
print (FN + LN)

s = "lghlkgkfdgjlsdkjhfgsjafgk"
print (len (s))

squares = [1, 4, 9, 16, 25]
print (squares)
print (squares[0])
print (squares[3])
print (squares[-1])
print (squares[-3:])

x = 9
y = x/2
y = x//2
y = x**2
print (y)

temperatura = 15
czy_szczesliwy = False
if not temperatura > 10 or czy_szczesliwy:
   print ("wychodzimy")
elif temperatura > -10 and czy_szczesliwy:
   print ("ubierz się ceiepło")
else:
   print ("nie wychodzimy")

for i in range (10):
   print (i)

for i in range (10):
   print ("i")

for i in range (1,10):
   print (i)

for i in range (1,10, 2):
   print (i)

x = "cieplo"
temp = 15
while temp > 10:
   print ("temperatura jest ok", temp, x)
   temp = temp -1

oceny = [4, 5, 3, 2, 1, 6, 5, 4]
oceny_marka = [3, 2, 3, 2, 1, 2, 1, 3]
oceny_kozaka = [4, 5, 6, 5, 5, 6, 5, 3]

marek_set = set(oceny_marka)
kozak_set = set(oceny_kozaka)
print(kozak_set.difference(marek_set))

oceny = list(set(oceny))
print(oceny)

oceny_all = ([4, 5, 3, 2, 5], [4, 3, 2, 5], [5, 4, 3])

oceny_slownik = {}
oceny_slownik["marek"] = [4, 5, 3, 2, 5]
oceny_slownik["kozak"] = [4, 3, 2, 5]
print (oceny_slownik["marek"])

for k,v in oceny_slownik.items():
   print(k,v)

name = "Wojtek"
for letter in name:
   print (letter)

name = "Wojtek"
name = name.upper()
print(name)
name = name.lower()
print(name)
print (len(name))

if "W" in name:
    print ("jest taka literka")

name = name.replace("tek", "ciul")
print(name)

test_string = "ala ma kota i jd"
test_string = test_string.replace(" ","*")
test_string = test_string.split("*")
print(test_string)

with open("plik.txt"):
    print
