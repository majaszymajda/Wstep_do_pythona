from math import log


class LogExp():
    def __init__(self, a):
        self.a = a

    def logax(self, x):
        return log(x, float(self.a))

    def ax(self, x):
        return a*x  # mnozenie
        # return a**x  # potegowanie


a = float(input("podaj a : "))
logexp = LogExp(a)
print(a)

while True:
    x = float(input("podaj x: "))
    print("logarytm a z x = {}".format(logexp.logax(a)))
    print("mnozenie a*x = {}".format(logexp.ax(x)))
    print("by zamknac wcisnij ctrl d :) ")
