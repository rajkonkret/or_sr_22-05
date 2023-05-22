a = 8
b = 7


def dodaj():
    print(a + b)


def dodaj2(a, b, c=0):
    print(a + b - c)


def mnozenie(a, b):
    return a * b


dodaj()
dodaj2(5, 4)
dodaj2(5, 4, 7)
dodaj2(c=5, a=4, b=7)
# zwraca None
print(dodaj())
print(mnozenie(4, 5))
