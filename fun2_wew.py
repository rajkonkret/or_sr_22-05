def f():
    def fwew(a, b):
        return (a * b)

    return fwew  # zwroci adres funkcji


# nazwa_funkcji() - uruchomienie funkcji
x = f()
print(x)
print(x(5, 6))

