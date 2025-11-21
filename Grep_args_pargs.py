#python grep.py "szukany tekst" plik1.txt plik2.txt

import argparse


def main():
    parser = argparse.ArgumentParser(description="Prosty grep w Pythonie")
    parser.add_argument("pattern", help="Tekst do wyszukania")
    parser.add_argument("files", nargs="+", help="Pliki do przeszukania")
    parser.add_argument("--reserved", action="store_true", help="Pokazuje linie, które NIE zawierają wzorca")

    args = parser.parse_args() #parametry pozycjonalne (biblioteka args, pargs)
    pattern = args.pattern
    reserved = args.reserved
    print (pattern)

    files = args.files
    print (files)

    licznik = 0


    for file_name in files:
        try:

            with open(file_name) as f:
                line_number = 0
                licznik_plik = 0
                for line in f:
                    line_number+=1
                    if reserved == False and pattern in line:
                        print ((f'{file_name}, Tekst, {line.rstrip()}, w Linii numer:  ,{line_number} \n'))
                        licznik += 1
                        licznik_plik += 1
                    elif reserved == True and pattern not in line:
                        print((f'{file_name}, Tekst, {line.rstrip()}, w Linii numer:  ,{line_number} \n'))
                        licznik += 1
                        licznik_plik += 1
                print (f'fbaskjbfkj, {file_name}, {licznik_plik}')
        except FileNotFoundError:
            print(f"Błąd: plik {file_name} nie istnieje")
        except Exception as e:
            print(f"Błąd podczas czytania pliku {file_name}: {e}")
    print ('Liczba dopasowanych wszystkich wyników:', licznik)



if __name__ == "__main__":
    main()


