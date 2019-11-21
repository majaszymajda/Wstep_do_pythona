from datetime import datetime
print("Roznica dni wynosi: " )

def liczenie_dni_pomiedzy(data1, data2):
    data1 = datetime.strptime(data1, "%Y-%m-%d")
    data2 = datetime.strptime(data2, "%Y-%m-%d")
    roznica_dat = abs((data2 - data1).days)
    return print ({roznica_dat})
    
