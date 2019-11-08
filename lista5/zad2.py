class student():
    def __init__(self, imie, nazwisko, nr_albumu, grupa="A", rok=2019, pije=True):
        self.imie = imie
        self.nazwisko = nazwisko
        self.grupa = grupa
        self.nr_albumu = nr_albumu
        self.rok = rok
        self.pije = pije

    def __str__(self):
        return "{} {} Grupa {} {} {} {}".format(
            self.imie,
            self.nazwisko,
            self.grupa,
            self.nr_albumu,
            self.rok,
            ("Pije" if self.pije else "Abstynent")
        )


andrzej = student("Andrzej", "Kowalski ", 454545)
anna = student("Anna", "Jankowska", 545454, grupa="B", pije=False)

print(andrzej)
print(anna)