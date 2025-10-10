student = {
    "imie": "Anna",
    "wiek": 22,
    "kierunek": "Informatyka"
}
print(student["imie"])  # Anna
print(student.get("wiek"))  # 22

student ["imie"] = "Karol"
print(student["imie"])

student["Location"] = "Wrocław"
print (student["Location"])

print (student)
del student["wiek"]

for klucz, wartosc in student.items():
    print(f"{klucz} → {wartosc}")

liczby = {1, 2, 3, 3, 4}
print(liczby)  # {1, 2, 3, 4}

liczby.add(5)
liczby.remove(2)

for x in liczby:
    print(x)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # suma: {1, 2, 3, 4, 5}
print(a & b)  # przecięcie: {3}
print(a - b)  # różnica: {1, 2}

owoce = {"jabłko", "banan", "gruszka"}

if "banan" in owoce:
    print("Banan jest w zbiorze.")
else:
    print("Banana nie ma w zbiorze.")

def isIsogram(word):
    char_set = set()
    for c in word:
        if c.isalpha() == False:
            continue
        if c in char_set:
            return False
        else:
            char_set.add(c)
    return True

word = "six-years-old"

result = isIsogram(word)
if result == True:
   print(f"{word} Yes")
else:
   print(f"{word} No")
print("\n\n")
word = "bcmmaass"
result = isIsogram(word)

if result == True:
   print(f"{word} Yes")
else:
   print(f"{word} No")

