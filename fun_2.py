def example(a, b, **kwargs):  # **kwargs - argumenty słownikowe
    print(a, b)
    print(kwargs)
    return a * b


print(type(example))
print(example.__code__.co_varnames)

print(example(1, 2, c="Radek", l=8))

# lamda

liczymy = lambda x, y: x * y
print(liczymy(200, 50))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 20, 55]
# map()  - pobiera elementy z listy i wykonuje działanie za pomocanp.: lambdy
print(f"Użycie map() {list(map(lambda x: x * 2, lista))}")
# filter()

print(f"Użycie filter() {list(filter(lambda x: x < 5, lista))}")
