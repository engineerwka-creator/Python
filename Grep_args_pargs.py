#python grep.py "szukany tekst" plik1.txt plik2.txt

import argparse


def main():
    parser = argparse.ArgumentParser(description="Prosty grep w Pythonie")
    parser.add_argument("pattern", help="Tekst do wyszukania")
    parser.add_argument("files", nargs="+", help="Pliki do przeszukania")

    args = parser.parse_args() #parametry pozycjonalne (biblioteka args, pargs)
    pattern = args.pattern
    print (pattern)

    files = args.files
    print (files)

    for file_name in files:
        with open(file_name) as f:
            line_number = 0
            for line in f:
                line_number+=1
                if pattern in line:
                    print (f'{file_name}, Tekst, {line.rstrip()}, w Linii numer:  ,{line_number} \n')




if __name__ == "__main__":
    main()


