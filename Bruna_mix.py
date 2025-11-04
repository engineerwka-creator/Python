stan_konta = int (input("podaj stan konta "))
stan_konta = ((stan_konta) + 500)
print (stan_konta)

person = {"name": "Kate", "age": 19}
print (person)

p = "5"
r = p.isalnum()
print (f"{r}")

convert = int(p)
print (p)

def Halo(name):
    print ("Karol")

def Uczelnia(name):
    print ("Polytechnic")

#Obliczamy resztę z dzielenia:
a = 6
b = 3
print (a % b) #0

c = 5
d = 2
print (c % d) #1

#Wskazujemy na typy liczb int (4) czy float (4.0).

print (type (a + b))
print (type (a - b))
print (type (a * b))
print (type (a / b))

#Pętla for z dwoma warunkami

oceny = [1, 2, 3, 4, 5, 6, 7]
for y in oceny:
    if y <= 5:
        print('Kliczko')
    else:
        print ('Lord of the Ring')

print(f"The next number is {a + 1}")
