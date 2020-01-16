import pickle
import datetime

def wpisywanie_tekstu(wpis):
    pamietnik = open("pamietnik.txt", 'ab')
    czas = datetime.datetime.now()
    data = czas.strftime("%x"), czas.strftime('%X')

    wpisy = []
    wpisy.append([data, wpis])

    pickle.dump(wpisy, pamietnik)
    pamietnik.close()

def wypisywanie():
    pamietnik = open("pamietnik.txt", 'rb')
    while 1:
        try:
            teksty = pickle.load(pamietnik)
            print(teksty)
        except (EOFError):
            break

    pamietnik.close()


print("Witaj, czekam na Twoj nowy wpis :)  ")
wpis = input()

wpisywanie_tekstu(wpis)
wypisywanie()
