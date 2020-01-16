import re

numertelefonu = '(600-700-8001)'
wzor = re.compile(r'\d{3,4}')
zmiana = wzor.finditer(numertelefonu)

for i in zmiana:
    print("'", i.group() + "'")