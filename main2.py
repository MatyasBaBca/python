from datetime import datetime

class Car:
    def __init__(self, značka, rok_výroby, model, palivo):
        self.značka = značka
        self.rok_výroby = rok_výroby
        self.model = model
        self.palivo = palivo

    def vypsat_informace(self):
        print(f"Značka: {self.značka}, Rok výroby: {self.rok_výroby}, Model: {self.model}, Palivo: {self.palivo}")

    def věk_auta(self):
        aktuální_rok = datetime.now().year
        věk = aktuální_rok - self.rok_výroby
        return věk

auto1 = Car("Toyota", 2018, "Corolla", "Benzín")
auto2 = Car("Ford", 2015, "Focus", "Nafta")
auto3 = Car("Honda", 2020, "Civic", "Elektřina")

auto1.vypsat_informace()
print(f"Věk auta: {auto1.věk_auta()} let\n")

auto2.vypsat_informace()
print(f"Věk auta: {auto2.věk_auta()} let\n")

auto3.vypsat_informace()
print(f"Věk auta: {auto3.věk_auta()} let\n")
