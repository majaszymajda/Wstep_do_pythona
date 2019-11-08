import random


class liczba_losowa():
    def losuj_liczby(self):
        return random.random()


class wykladnicza(liczba_losowa):
    def losuj_liczby(self):
        return random.expovariate(5)


class gaussa(liczba_losowa):
    def losuj_liczby(self):
        return random.gauss(0, 1)


class stala(liczba_losowa):
    def losuj_liczby(self):
        return 42


x = liczba_losowa()
y = wykladnicza()
z = gaussa()
a = stala()

for i in [x, y, z, a]:
    print(i.losuj_liczby())
