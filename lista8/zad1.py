import re
import os 


lokalizacjapierwsza = input("wproewadz scieszke w ktorej bedziesz szukal pracy: ")


def szukamPracy(nazwaPliku, ścieżkaPliku):
    szukam = re.search('.*praca.*(\.pdf)$', nazwaPliku)

    if szukam:
        nazwa = szukam.group()
        print(os.path.join(ścieżkaPliku, nazwa))


for i in os.walk(lokalizacjapierwsza):
    for nazwaPliku in i[2]:
        szukamPracy(nazwaPliku, i[0])