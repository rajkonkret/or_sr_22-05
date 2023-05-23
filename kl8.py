class Car:
    """
    To jest klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print("Predkość w km/h ", self.__predkosc)

    def hamuj(self):
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("zmiana biegu")


c1 = Car("Tesla", 2018)
c1.gaz()
c1.gaz()
c1.gaz()
c1.gaz()
c1.gaz()
# print(c1.predkosc) - nie mozna wykonac bo pole oznaczone jako prywatne __
c1.licznik()
c1.licznik()
c1.hamuj()
c1.hamuj()
c1.hamuj()
c1.hamuj()
c1.hamuj()
c1.licznik()
