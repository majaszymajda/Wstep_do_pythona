import re


numertelefonu = '(111-22-33)'
zmiana = re.sub(r'[-()]+', '', numertelefonu)

print(zmiana)