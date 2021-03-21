x = int(input("Podaj szerokość: "))
y = int(input("Podaj długość: "))
class Prostokat:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def pole(self):
        wynik1 = self.__a * self.__b
        return wynik1
    def obowod(self):
        wynik = 2 * self.__a + 2 * self.__b
        return wynik

p1 = Prostokat(x, y)
obwod_protokata = p1.obowod()
pole_prosotkata = p1.pole()
print(obwod_protokata)
print(pole_prosotkata)

print("a: ", p1.__a, "b: ", p1.__b)