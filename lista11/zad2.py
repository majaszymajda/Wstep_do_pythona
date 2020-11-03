import sqlite3  # baza sqlite


def usun_studenta(c, id):
    zapytanie = f'DELETE from studenci WHERE id={id}'
    c.execute(zapytanie)


def pokaz_studentow_uczelni(c, id):
    zapytanie = f'SELECT * from studenci where uczelnia_id={id}'
    c.execute(zapytanie)
    print(c.fetchall())  # wypsuje id i nazwe uczelni


def pokaz_uczelnie(c):
    zapytanie = 'SELECT * from uczelnie'
    c.execute(zapytanie)
    print(c.fetchall())  # id i nazwe uczelni


def stworz_uczelnie(c, nazwa):
    zapytanie = 'INSERT INTO uczelnie(nazwa) VALUES(?)'
    c.execute(zapytanie, nazwa)  # dodajemy uczelnie o podanej nazwie


def stworz_studenta(c, student):
    zapytanie = 'INSERT INTO studenci(imie, nazwisko, uczelnia_id) VALUES(?, ?, ?)'
    c.execute(zapytanie, student)


if __name__ == "__main__":
    conn = sqlite3.connect('baza.db')
    c = conn.cursor()  # obiekt do operacji na bazie danych

    # tworzy dwie tabele w bazie danych
    # uczelnie
    c.execute('''CREATE TABLE IF NOT EXISTS uczelnie (
       id integer PRIMARY KEY,
       nazwa text
   )''')
    # studentow
    c.execute('''CREATE TABLE IF NOT EXISTS studenci (
       id integer PRIMARY KEY,
       imie text,
       nazwisko text,
       uczelnia_id integer,
       FOREIGN KEY (uczelnia_id) REFERENCES uczelnie(id)
   ) ''')
    # FOREIGN KEY oznacza relacje wielu studentow do jednej uczelni

    stworz_uczelnie(c, ['Politechnika Wrocławska'])
    stworz_uczelnie(c, ['Uniwersytet Wrocławski'])

    student1 = ('Anna', 'Kowalska', 1)
    student2 = ('Jan', 'Nowakowski', 1)
    student3 = ('Alicja', 'Banek', 2)

    stworz_studenta(c, student1)
    stworz_studenta(c, student2)
    stworz_studenta(c, student3)

    print('Uczelnie')
    pokaz_uczelnie(c)

    print('Studenci politechniki')
    pokaz_studentow_uczelni(c, 1)  # Politechnika wroclawska studenci
    print('Studenci Uniwersytetu')
    pokaz_studentow_uczelni(c, 2)  # Uniwersytet studenci

    usun_studenta(c, 1)
    print('Po usunieciu na politechnice zostal')
    pokaz_studentow_uczelni(c, 1)