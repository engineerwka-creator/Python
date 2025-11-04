import means
import csv

if __name__ == "__main__":
    print ("Karol i Marcin")

    sum4 = means.mean_arthmetic2([1, 2, 3, ])
    sum5 = means.mean_arthmetic2([4, 5, 6, ])
    sum6 = means.mean_arthmetic2([9, 10, 11, ])
    print("sum4, sum5, sum6 ", sum4, sum5, sum6)

with open('C:\\Users\\engin\\Downloads\\oceny_uczniow.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  # każda linia jako lista



dane = [
    ['Imię', 'Nazwisko', 'Wiek'],
    ['Anna', 'Kowalska', 30],
    ['Jan', 'Nowak', 25]
]

with open('C:\\Users\\engin\\Downloads\\nowy_plik.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dane)

s_means_min = 7
s_means_max = 0
s_surname = ""
sx_surname = ""

with open('C:\\Users\\engin\\Downloads\\oceny_uczniow.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Nazwisko'], row['Matematyka'])  # dostęp przez nazwę kolumny
        print (row)

        s_means = means.mean_arthmetic2([int (row ['Matematyka']), int (row ['Polski']), int (row ['Biologia'])])
        if s_means_max < s_means:
            s_means_max = s_means
            s_surname = row ['Nazwisko']
        if s_means_min > s_means:
            s_means_min = s_means
            sx_surname = row['Nazwisko']
    print ("s_means_max", s_means_max, s_surname)
    print("s_means_min", s_means_min, sx_surname)
