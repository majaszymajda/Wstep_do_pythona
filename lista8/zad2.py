import re


tekst = 'labpyt2019@gusun_tomail.pl'
zmiana = re.search('(.*)usun_to(.*)', tekst)

if zmiana:
    wynik = tekst.replace('usun_to', '')
    print(wynik)