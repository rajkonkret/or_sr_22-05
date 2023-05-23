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

liczymy = lambda x, y: x * y - 1
print(liczymy(5, 6))
r0 = {'miasto': 'Kielce'}
r1 = {'miasto': 'Kielce', 'ZIP': "25-900"}

d_zip = lambda row: row.setdefault('ZIP', '00-000')
print(d_zip(r0))
print(r0)
print(d_zip(r1))
print(r1)

lata = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
        (2004, 31.33), (2008, 32.84), (2009, 33.02), (2010, 32.92)]

print(max(lata))    # (2010, 32.92)
print(max(lata, key=lambda c: c[1]))
print(max(map(lambda c: (c[1], c), lata)))
print(max(map(lambda c: (c[1], c), lata))[1])
print(max(map(lambda c: (c[1], c), lata))[0])

