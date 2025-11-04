class Samochod:
    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    def pokaz_info(self):
        print(f"Samochód: {self.marka} {self.model}  {self.rok_produkcji} {self.przebieg}")

    def zmniejsz_przebieg(self):
        self.przebieg -= 200

    def __str__(self):
       return f"Samochód: {self.marka} {self.model}  {self.rok_produkcji} {self.przebieg}"

    def __eq__(self, inny_samochod):
       return self.marka == inny_samochod.marka and self.model == inny_samochod.model and self.rok_produkcji == inny_samochod.rok_produkcji and self.przebieg == inny_samochod.przebieg

auto1 = Samochod("Toyota", "Corolla", "1999", 2000)
auto2 = Samochod("Ford", "Focus", "1989", 1000)
auto3 = Samochod("Tesla", "Model X", "2023", 500)
if auto1 == auto1:
    print ("Auta są takie same")
else:
    print ("Auta nie są takie same")

auto1.pokaz_info()
auto2.pokaz_info()

auto1.zmniejsz_przebieg()
auto2.zmniejsz_przebieg()

auto1.pokaz_info()
auto2.pokaz_info()
#
print (auto1)

