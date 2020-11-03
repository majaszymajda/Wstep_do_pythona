import dbm  

# ta baza danych jest oparta na kluczach

if __name__ == "__main__":
    with dbm.open('baza_danych', 'c') as baza:
        # zapisuje imie w bazie jako bajty
        baza['moje_imie'] = 'Anna'
        baza['nazwisko'] = 'Nowak'
        baza['numer albumu'] = '123456'
        baza['nazwa uczelni'] = 'PWR'

        print(baza['moje_imie'].decode( 'UTF-8'))  # odczytuje, funkcji decode i standardu UTF-8 żeby otczytać imie zapisane w bajtach bez prefixu b
        print(baza['moje_imie'])  

        #print(baza['moje_nazwisko'].decode('UTF-8'))

        print(baza['nazwisko'])

        #print(baza['numer albumu'].decode('UTF-8'))

        print(baza['numer albumu'])

        #print(baza['nazwa uczelni'].decode('UTF-8'))

        print(baza['nazwa uczelni'])
